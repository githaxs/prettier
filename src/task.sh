#!/usr/bin/env bash
set -e

run_prettier() {
    if [[ $1 =~ .*.(js|ts|scss|css|yaml|yml|html|jsx)$ ]]; then
        prettier --write --config ../.prettierrc.json $1
    fi
}

task() {
    foreach_changed_file run_prettier
}
