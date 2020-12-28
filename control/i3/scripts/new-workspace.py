#!/usr/bin/env python3

import json
import subprocess as sp
from sys import argv, exit

# Programs that should be contained in a single workspace each
prevent_multi_ws = ['zathura', 'zotero', 'palemoon']
# Programs (typically from the list above), to which additionally the tabbed layout should be applied
tabbed = ['zathura']


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


##!/bin/sh -e
#i3-msg workspace $(($(i3-msg -t get_workspaces | tr , '\n' | grep '"num":' | cut -d : -f 2 | sort -rn | head -1) + 1))
