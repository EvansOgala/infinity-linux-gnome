#!/bin/bash
modprobe zram
zramctl -a zstd -s 5G /dev/zram0
mkswap /dev/zram0
swapon --prio 100 /dev/zram0

