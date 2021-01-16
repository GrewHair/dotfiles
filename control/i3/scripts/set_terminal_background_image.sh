#!/bin/bash

pid=$(xprop -id `xdotool getwindowfocus` | grep '_NET_WM_PID' | grep -oE '[[:digit:]]*$')
socket=$(grep $pid /tmp/kitties | cut -d ";" -f 2)
background_image=$(sxiv -t -o /home/boris/.local/share/kitty/background_images/ | xargs)
kitty @ --to "$socket" set-background-image "$background_image"

exit 0
