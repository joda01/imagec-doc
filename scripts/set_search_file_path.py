import yaml

def read_base_url_from_yaml(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        
        base_url = data.get('baseurl')
        if base_url is not None:
            print(f"baseurl: {base_url}")
            return base_url
        else:
            print("Key 'baseurl' not found in the YAML file.")
            return ""
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return ""
    except yaml.YAMLError as e:
        print(f"YAML parsing error: {e}")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""




def replace_baseurl(file_path: str, old: str = "{{ site.baseurl }}", new: str = "/myName") -> None:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        updated_content = content.replace(old, new)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"Replaced '{old}' with '{new}' in '{file_path}'.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#
# Set base URL in search.js file
#
baseUrl = read_base_url_from_yaml("_config.yml")
replace_baseurl("_site/js/search.js","{{ site.baseurl }}", baseUrl)
