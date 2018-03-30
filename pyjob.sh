#!/bin/bash

cur_dir="$(dirname "${BASH_SOURCE[0]}")"

if [ -f "${cur_dir}/main.py" ];
then
    echo "Setup alias 'pyjob'"
    alias pyjob="python3 '${cur_dir}/main.py'"
fi