#!/bin/bash

# title="$1"
# title="$(echo $1 | tr _ \ )"
title=" "
# path="\"/home/boris/bin/i3/notifications/"$1"\""
# path="/home/boris/bin/i3/notifications/$1"
notification="$(cat /home/boris/bin/i3/notifications/$1)"
# killall dunst
dunstctl close-all
notify-send "$title" "$notification"

exit 0
