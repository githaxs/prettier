#!/usr/bin/env bash
set -e

run_prettier() {
    config=""
    if [ -f ../.format_config.json ]; then
        config="--config ../.format_config.json"
    fi

    if [[ $1 =~ .*.(js|ts|scss|css|yaml|yml|html|jsx)$ ]]; then
        prettier --write "$config" "$1"
    fi
}

task() {
    foreach_changed_file run_prettier
}
