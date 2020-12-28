#!/bin/bash

caps_state="$(xset q | grep Caps | grep -P '(?<=Caps Lock:).*(?=01: Num Lock)' -o | xargs)"

if [ "$caps_state" == "on" ]; then
	xdotool key Caps_Lock
fi

exit 0
