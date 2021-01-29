#!/usr/bin/env python3

import subprocess as sp
from sys import argv, exit
import os

# Get the command to be sent to playerctl from the argument
command = argv[1]

# playerctl doesn't always register pids of mpv instances - i.e. for the first instance launched it may
# just write 'mpv' instead of 'mpv.instanceXXXXXX'. Therefore directly polling pids may result in an error
# I'll keep the next line around and commented out for later. For now it's better to just poll playerctl directly since
# I don't want to call anything else then just playerctl.
#players_pidof = sp.check_output('pidof mpv', shell=True, text=True).strip().split(' ')

# Get all players set (mpv in this case)
players = set(sp.check_output('playerctl --list-all | grep "mpv"', shell=True, text=True).strip().split('\n'))

# Get the hypothesized player under focus through concatenating 'mpv.instance' with the pid of the currently focused window
# TODO deal with the fact that the playerctl's list may not necessarily contain the pid (see above) - in which case
# this protective mechanism fails
player_under_focus = 'mpv.instance' + sp.check_output("xprop -id `xdotool getwindowfocus` | grep '_NET_WM_PID' | grep -oE '[[:digit:]]*$'", shell=True, text=True).strip()

# Remove the player under focus from the players set to allow manual-only control of it (since it's under focus :D)
if player_under_focus in players:
    players.remove(player_under_focus)

# Get the list of currently playing players by polling playerctl based on the players set
# TODO rewrite this as a list comprehension
# TODO the resulting list comprehension would be too long for a one-liner anyway - so dig into how to format it using multiple lines (that's a pretty freaking general and irritating problem of yours)
playing = []
for player in players:
    if sp.check_output(f"playerctl -p {player} status", shell=True, text=True).strip() == 'Playing':
        playing.append(player)

# If some players from the set are playing, and the command is "play-pause", stop all of them, write one of them into a temp file, and exit
if playing and command == "play-pause":
    for player in playing:
        os.system(f"playerctl -p {player} {command}")
    os.system(f"echo {playing[0]} > /tmp/recent-player")
    exit()

# If some players from the set are playing, and the command is *not* "play-pause", just run the command on the first of the playing players and exit
if playing and command != "play-pause":
    os.system(f"playerctl -p {playing[0]} {command}")
    exit()

# Read the temp file to get the recently stopped player's playerctl identifier (the fallback is simply mpv)
# TODO replace the hardlink to the temp file with a proper path variable
try:
    with open('/tmp/recent-player', 'r') as rp:
        recent_player = rp.readlines()
except: recent_player = ['mpv']

# TODO get rid of this by including it in the above line (I'm unsure if it will work)
recent_player = recent_player[0].strip()

if not playing and command == "play-pause":
    os.system(f"playerctl -p {recent_player} {command}")

exit()
