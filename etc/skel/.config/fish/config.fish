if status is-interactive
# Commands to run in interactive sessions can go here
source (/usr/bin/starship init fish --print-full-init | psub)
fish_add_path ~/.local/bin
fastfetch
echo Infinity Linux 2026.8
end
