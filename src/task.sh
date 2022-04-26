#!/usr/bin/env bash
set -e

run() {
    if [[ $1 =~ .*\.(js|ts|scss|css|yaml|yml|html|jsx)$ ]]; then
        prettier --write $1
    fi
}

task() {
    echo "Running Task..."

    foreach_changed_file run
}
