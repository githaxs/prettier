#!/usr/bin/env bash
set -e

PRETTIER_CONFIG=${PRETTIER_CONFIG:-""}

run() {
    if [[ $1 =~ .*\.(js|ts|scss|css|yaml|yml|html|jsx)$ ]]; then
        echo "Running prettier on $1"
        prettier --write "$1" > /dev/null
    fi
}

task() {
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

    foreach_changed_file run

    # Restore original .prettierrc if it existed
    # so the task doesn't fail due to changes to
    # the config file.
    git checkout .prettierrc || true
}
