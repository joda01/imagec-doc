#pip install marko
#pip install frontmatter
# pip install -r requirements.txt
# gem install "jekyll-theme-minima"
# gem install minima

# Pre build
python3 ./scripts/read_version_information.py
python3 ./scripts/find_conflicting_redirects.py
python3 ./scripts/find_misaligned_titles.py
python3 ./scripts/generate_llms_txt.py
python3 ./scripts/docs_link_fixer.py
python3 ./scripts/use-link-tags.py
#python3 ./scripts/generate_search.py

# build
bundle exec jekyll build --config _config.yml,_config_exclude_archive.yml

