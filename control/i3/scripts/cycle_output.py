#!/usr/bin/env python3
import json
import subprocess as sp
from sys import argv
import i3ipc

target_output = argv[1]
direction = argv[2]

get_ws_cmd = 'i3-msg -t get_workspaces'
ws = json.loads(sp.run(get_ws_cmd, shell=True, stdout=sp.PIPE).stdout)
current_output = [w for w in ws if w['focused']][0]['output']

# Move the window marked as 'teleport' to the target output, if it is focused
i3 = i3ipc.Connection()
focused = i3.get_tree().find_focused()
if 'teleport' in focused.marks:
    sp.run('i3-msg move container to output ' + target_output, shell=True)

#sp.run('i3-msg ')
if current_output != target_output:
    sp.run('i3-msg focus output ' + target_output, shell=True)
else:
    sp.run('i3-msg [workspace=shared] move workspace to output ' + target_output, shell=True)
    sp.run('i3-msg workspace ' + direction + '_on_output', shell=True)
