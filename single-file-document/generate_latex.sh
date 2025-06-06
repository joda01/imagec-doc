#!/usr/bin/env bash

set -xeuo pipefail

# navigate to the directory of the script
cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

python3 concatenate_to_single_file.py
pandoc --defaults pandoc-configuration.yaml --to=latex --output imagec-doc.tex
