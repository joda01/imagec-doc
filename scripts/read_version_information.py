import requests
import json
import os
import yaml
from collections import defaultdict



def sync_version(yaml_file, version, sha256, dateTime):
    # Load YAML file
    with open(yaml_file, 'r') as yf:
        yaml_data = yaml.safe_load(yf)

    # Update release in YAML
    yaml_data['current_short_imagec_version'] = version
    yaml_data['preview_short_imagec_version'] = version
    yaml_data['current_imagec_version'] = version
    yaml_data['current_imagec_hash'] = sha256

    # Write updated YAML back
    with open(yaml_file, 'w') as yf:
        yaml.safe_dump(yaml_data, yf, sort_keys=False)


def write_version_to_json(json_file, version, sha256, dateTime):
    # Load YAML file
    with open(json_file, 'r') as jf:
        json_data = json.load(jf)

    # Update release in YAML
    json_data['version'] = version
    json_data['timestamp'] = dateTime
    json_data['sha256'] = sha256

    # Write updated YAML back
    with open(json_file, 'w') as jf:
        json.dump(json_data, jf, sort_keys=False)


def read_version():
    # Configurable GitHub repo
    owner = "joda01"
    repo = "imagec"

    # GitHub API URL for latest release
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"

    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"Bearer {token}"} if token else {}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch release data: {response.status_code} {response.text}")

    data = response.json()

    outData = defaultdict(dict)

    for asset in data["assets"]:
        key="no"
        if asset["name"] == "imagec-arm64-macos-cpu-bundle.zip":
            key="macoscpu"
        if asset["name"] == "imagec-x64-linux-cpu-bundle.zip":
            key="linuxcpu"
        if asset["name"] == "imagec-x64-linux-cuda-bundle.7z":
            key="linuxcuda"   
        if asset["name"] == "imagec-x64-win-cpu-bundle.zip":
            key="wincpu"   
        if asset["name"] == "imagec-x64-win-cude-bundle.7z":
            key="wincuda"   

        outData[key]["name"] = asset["name"]
        sizeMB = float(asset["size"])/1000000
        if sizeMB < 1000:
            outData[key]["size"] = str(int(sizeMB))+" MB"
        else:
            size = sizeMB/1000
            outData[key]["size"] = f"{size:.2f} GB"

        outData[key]["sha256"] = asset["digest"]
        outData[key]["download"] = asset["browser_download_url"]
    
    outData["version"] = data.get("tag_name")
    outData["timestamp"] = data.get("published_at")
    # Write the dynamic JSON object to file
    with open("_data/releases.json", "w") as f:
        json.dump(outData, f, indent=4)

    sync_version("_config.yml", data.get("tag_name"), "", data.get("published_at"))



print("Update versions ...")
read_version()
print("Update versions finished ...")