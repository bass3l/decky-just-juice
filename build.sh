#!/usr/bin/env bash
CLI_LOCATION="$(pwd)/cli"
echo "Building plugin in $(pwd)"
printf "Please input sudo password to proceed.\n"

sudo $CLI_LOCATION/decky plugin build $(pwd) --output-filename-source directory

sudo chown -R deck:deck ./out

sudo bsdtar -C /home/deck/homebrew/plugins -xzpf out/decky-just-juice.zip

sudo chown -R deck:deck /home/deck/homebrew/plugins/decky-just-juice

sudo systemctl restart plugin_loader
