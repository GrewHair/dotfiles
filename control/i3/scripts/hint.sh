#!/bin/bash

scrot -o --focused /tmp/hint-scrot.png
data=$(tesseract /tmp/hint-scrot.png stdout tsv)
boxes=$(echo "$data" | grep ^3 | awk '{split("QWERTYUIOP[]ASDFGHJKL;ZXCVBNM/", foo, ""); print "rectangle "$7","$8" "$9+$7","$10+$8" text "$7-30","$8+25" "foo[FNR]}')  # maybe FNR instead of $3?
pos=$(xdotool getwindowfocus getwindowgeometry | grep Position | grep -P "[0-9]*,[0-9]*" -o)
geom=$(xdotool getwindowfocus getwindowgeometry | grep Geometry | grep -P "[0-9]*x[0-9]*" -o)
convert -size $geom xc:none -pointsize 30 -fill none -stroke green -strokewidth 3 -draw "$boxes" -pointsize 30 /tmp/hint-boxes.png
pqiv -c --window-position=$pos --zoom-level=0.9999999 --class=pqiv_hint /tmp/hint-boxes.png &
# sleep 0.4
# xdotool set_window --class=pqiv_hint $(xdotool getactivewindow)
echo "$data" > /tmp/hint-data

exit 0
