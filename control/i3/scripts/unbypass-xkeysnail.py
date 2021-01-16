#!/usr/bin/env python3

import subprocess as sp
import os

win_id = sp.check_output('xdotool getactivewindow', shell=True, text=True).strip()
curr_class = sp.check_output(f"xprop -id {win_id} WM_CLASS", shell=True, text=True).strip().split(' ')[-1].replace('"', '').replace("'", "")
new_class = curr_class.replace('_bypass', '')
os.system(f"xdotool set_window --class={new_class} {win_id}")

# #!/bin/bash

# win_id=$(xdotool getactivewindow)
# curr_class=$(xprop -id "$win_id" WM_CLASS | grep -P '(?<=, ").*(?="$)' -o)
# xdotool set_window --class="${curr_class:0:-7}" "$win_id"

# exit 0
