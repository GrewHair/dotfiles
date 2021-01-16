#!/usr/bin/env python3

import os
import subprocess as sp

wm_classes_to_bypass = ['Zotero', 'devtools']
win_id = sp.check_output("xdotool getactivewindow", shell=True, text=True).strip()
curr_class = sp.check_output(f"xprop -id {win_id} WM_CLASS", shell=True, text=True).strip().split(' ')[-1].replace('"', '').replace("'", "")
if curr_class in wm_classes_to_bypass:
    os.system(f"xdotool set_window --class={curr_class}_bypass {win_id}")

# #!/bin/bash

# win_id=$(xdotool getactivewindow)
# curr_class=$(xprop -id "$win_id" WM_CLASS | grep -P '(?<=, ").*(?="$)' -o)
# xdotool set_window --class="$curr_class"_bypass "$win_id"

# exit 0
