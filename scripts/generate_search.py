import os
import marko
import re
import json
from textwrap import shorten


skipped_files = [
    'docs/preview',
    'docs/stable/search.md',
    'docs/1.1',
    'docs/1.0',
    'docs/0.10',
    'docs/0.9',
    'docs/0.8',
]

file_list = []
skip_types = [marko.block.HTMLBlock, marko.inline.Image, marko.inline.InlineHTML]


def normal_whitespace(desc: str) -> str:
    return re.sub(r'\s+', ' ', desc.strip())


def extract_text(parse_node):
    if not hasattr(parse_node, 'children'):
        return ''
    if type(parse_node) in skip_types:
        return ''
    if type(parse_node.children) == type(''):
        return (
            parse_node.children.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        )
    result = ''
    for child in parse_node.children:
        result += ' ' + extract_text(child)
    return result


def sanitize_input(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'img\s+src\s+[^\s]+.*?(?=\s\w+\s|$)', ' ', text)
    return normal_whitespace(re.sub(r'[^\w\s_-]', ' ', text.lower())).strip()


def extract_blurb(parse_node):
    for child in parse_node.children:
        if type(child) == marko.block.Paragraph:
            return extract_text(parse_node)
    return ''


def sanitize_blurb(text):
    BLURB_THRESHOLD = 120
    text = re.sub(r'<img\s+[^>]*>', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = text.replace('"', '').strip()
    return shorten(text, width=BLURB_THRESHOLD, placeholder='...')


def sanitize_category(category):
    category = category.replace('_', ' ')
    if category == 'sql':
        return 'SQL'
    else:
        return category.title()


def get_url(fname):
    fname = '/' + fname.replace('.md', '')
    if fname.startswith('/_posts/'):
        url = re.sub(r'/_posts/(\d+)-(\d+)-(\d+)-(.*)', r'/\1/\2/\3/\4', fname)
    else:
        url = fname
    return url


def index_file(fname):
    if fname in skipped_files:
        return
    if not fname.endswith('.md'):
        return
    with open(fname, 'r') as f:
        text = f.read()
    splits = text.split('---', 2)
    if len(splits) != 3:
        print(f"No 3 splits for file '{fname}', missing header?")
        exit(1)
    title = ''
    text = ''
    blurb = ''
    category = ''

    if fname.startswith('docs/'):
        content_type = 'documentation'
    elif fname.startswith('_posts/'):
        content_type = 'blog'
    else:
        content_type = 'other'
    category = ''
    # parse header info
    lines = splits[1].split('\n')
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        line_splits = line.split(':', 1)
        if len(line_splits) != 2:
            continue
        if line_splits[0].strip().lower() == 'title':
            title = line_splits[1].strip()
            title = re.sub(r'^"|"$', '', title)
        if line_splits[0].strip().lower() == 'blurb':
            blurb = sanitize_blurb(line_splits[1].strip())
        if line_splits[0].strip().lower() == 'category':
            category = line_splits[1].strip()

    if len(title) == 0:
        print(f"No title found for file '{fname}' missing header?")
        exit(1)
    # parse main markdown file
    markdown_result = marko.parse(splits[2])
    text = extract_text(markdown_result)
    if len(blurb) == 0:
        blurb = sanitize_blurb(extract_blurb(markdown_result))
    if len(category) == 0:
        splits = fname.split(os.path.sep)
        category = sanitize_category(splits[len(splits) - 2])
    text = sanitize_input(text)
    file_list.append(
        {
            'title': title,
            'text': text,
            'category': category,
            'url': get_url(fname),
            'blurb': blurb,
            'type': content_type,
        }
    )


def index_dir(dirname):
    if dirname in skipped_files:
        return
    files = os.listdir(dirname)
    for file in files:
        full_path = os.path.join(dirname, file)
        if os.path.isfile(full_path):
            index_file(full_path)
        elif os.path.isdir(full_path):
            index_dir(full_path)


index_dir('docs')
index_dir('_posts')


# extract functions
def extract_markdown_text(text):
    parse_node = marko.parse(text)
    return extract_text(parse_node)


def sanitize_function(text):
    return (
        text.replace(' , ', ', ').replace('( ', '(').replace(' )', ')').replace("'", '')
    )


def sanitize_desc(text):
    return text.replace(' .', '.')


function_list = {}


def extract_functions(text, full_path):
    functions = re.findall(
        r'\n[|]([^|\n]+)[|]([^|\n]+)[|]([^|\n]+)[|]([^|\n]+)[|]', text
    )
    for function in functions:
        name = sanitize_function(
            normal_whitespace(extract_markdown_text(function[0].strip()).strip())
        )
        desc = (
            name
            + " - "
            + sanitize_desc(
                normal_whitespace(extract_markdown_text(function[1].strip()).strip())
            )
        )
        if '--' in name:
            continue
        if name.lower() in ('function', 'operator'):
            continue
        if 'alias' in desc.lower():
            continue
        name = re.sub(r'[(][^)]*[)]', '', name)
        function_list[name] = {
            'title': name,
            'text': normal_whitespace(desc.lower()),
            'category': os.path.basename(full_path).replace('.md', '').title()
            + " Functions",
            'url': '/' + full_path.replace('.md', ''),
            'blurb': sanitize_blurb(desc),
            'type': 'documentation',
        }


function_dir = os.path.sep.join('docs/stable/commands'.split('/'))

for root, dirs, files in os.walk(function_dir):
    files.sort()
    for file in files:
        full_path = os.path.join(root, file)
        with open(full_path, 'r') as f:
            text = f.read()
        extract_functions(text, full_path)

file_list.extend(function_list.values())

with open('data/search_data.json', 'w+') as f:
    json.dump({'data': sorted(file_list, key=lambda x: x['title'])}, f, indent='\t')

print("Search index file 'data/search_data.json' was generated successfully")
