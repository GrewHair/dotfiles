#!/bin/bash

if [ ! -f /tmp/launch_gvim ]; then echo yes > /tmp/launch_gvim; notify-send "zathura" "launch Gvim = yes"exit 0; fi

# if [ $(cat /tmp/launch_gvim) == yes ]; then echo no > /tmp/launch_gvim; else echo yes > /tmp/launch_gvim; fi
if [ $(cat /tmp/launch_gvim) == yes ]; then echo no > /tmp/launch_gvim; notify-send "zathura" "launch Gvim = no"; else echo yes > /tmp/launch_gvim; notify-send "zathura" "launch Gvim = yes"; fi

exit 0
