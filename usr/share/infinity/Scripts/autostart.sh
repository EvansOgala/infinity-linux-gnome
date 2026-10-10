#!/bin/bash

MARKER="$HOME/.config/infinity/.firstboot_done"

if [ ! -f "$MARKER" ]; then
    mkdir -p "$(dirname "$MARKER")"

    xdg-user-dirs-update --force
    if [ "$USER" = "live" ]; then
        pkexec calamares -d &
    fi

    if command -v plasma-welcome >/dev/null; then
        plasma-welcome &
    fi

    touch "$MARKER"
fi
