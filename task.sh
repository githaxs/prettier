#!/usr/bin/env bash
set -e

PRETTIER_CONFIG=${PRETTIER_CONFIG:-""}

run_task() {
    if [ "$PRETTIER_CONFIG" != "" ]; then
        # We want to only install the prettier config from NPM without
        # installing the rest of the dependencies in package.json.
        # To do this, we need to do the install in a different directory
        # and then move the folder to where the repo is.

        # See the comment on this thread: https://stackoverflow.com/a/52819886
        pushd /tmp > /dev/null

        export npm_config_cache=$(mktemp -d)
        npm install "$PRETTIER_CONFIG" > /dev/null
        popd > /dev/null
        mv /tmp/node_modules .
        echo "\"$PRETTIER_CONFIG\"" > .prettierrc
    fi

    echo "Running prettier"
    echo "Version: $(prettier --version)"
    FILES=$(echo "$1" | grep -E "\.(js|ts|scss|css|yaml|yml|html|jsx)$")
    prettier --write $FILES > /dev/null

    # Restore original .prettierrc if it existed
    # so the task doesn't fail due to changes to
    # the config file.
    #git checkout .prettierrc || true > /dev/null 

    if git diff > /dev/null; then
        echo '```diff'
        git diff
        echo '```'
        exit 1
    else
        exit 0
    fi
}
