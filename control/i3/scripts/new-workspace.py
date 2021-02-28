#!/usr/bin/env python3

import json
import subprocess as sp
import os
from sys import argv, exit

# Check the respect_layout flag
# TODO deal with the hardlink to the file
try:
    with open('/tmp/respect-layout', 'r') as rl:
        respect_layout = rl.readlines()[0].strip()
except:
    respect_layout = 'no'

# Exit if it is set
if respect_layout == 'yes':
    os.system('echo no > /tmp/respect-layout')
    exit()

# Programs that should be contained in a single workspace each
prevent_multi_ws = ['zathura', 'zotero', 'palemoon', 'mpv']

# Programs (typically from the list above), to which additionally the tabbed layout should be applied
tabbed = ['zathura', 'mpv']

# Programs that should be launched in background (i.e., without focusing their workspace)
prevent_focus = ['mpv']

# Get name of program to launch
try:
    program = argv[1]
except:
    program = None

# Get data from i3
get_ws_cmd = 'i3-msg -t get_workspaces'
ws = json.loads(sp.check_output(get_ws_cmd, shell=True))
ids = [ w['num'] for w in ws ]
nums_and_names = [ w['name'] for w in ws ]
names = [ x.split(': ')[1] if ': ' in x else '' for x in nums_and_names ]

# Find the smallest vacant workspace id
id = 1
while True:
    if id not in ids:
        break
    id+=1

# If no program is specified, just open a new workspace
if not program:
    sp.run('i3-msg workspace ' + str(id), shell=True)
    exit()

# If the specified program is in the 'single workspace' list and one instance/window of
# it is already present, override the workspace id with one of the already existing instance
if str(program) in prevent_multi_ws and str(program) in names:
    id = ids[names.index(str(program))]

# Move the program to the needed workspace and focus it
sp.run('i3-msg move to workspace "' + str(id) + ': ' + program + '"', shell=True)
sp.run('i3-msg workspace "' + str(id) + ': ' + program + '"', shell=True)

# If the program should be tabbed by i3, do it
if program in tabbed:
    sp.run('i3-msg layout tabbed', shell=True)

# If the program shouldn't be focused, go back to the original workspace
# (you had to bother to focus it in the first place because there seems to be
# no other way to set the layout to tabbed if needed)
if program in prevent_focus:
    sp.run('i3-msg "workspace back_and_forth"', shell=True)
