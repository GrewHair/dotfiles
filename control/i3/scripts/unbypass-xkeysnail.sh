#!/bin/bash

win_id=$(xdotool getactivewindow)
curr_class=$(xprop -id "$win_id" WM_CLASS | grep -P '(?<=, ").*(?="$)' -o)
xdotool set_window --class="${curr_class:0:-7}" "$win_id"

exit 0
