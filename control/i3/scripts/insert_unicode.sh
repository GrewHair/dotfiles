#!/bin/sh
#column -t ~/bin/insert_unicode.txt | rofi -theme solarized -dmenu -i -p "Icon" | cut -d ' ' -f 2 | xclip -sel clip
column -t ~/bin/insert_unicode.txt | rofi -theme solarized -dmenu -i -p "Insert Unicode" | tr -s ' ' | cut -d ' ' -f 2 | xclip -sel clip
xdotool key control+v
#xdotool key ctrl+shift+Insert # for vim (i'll do it later)
xdotool key BackSpace
