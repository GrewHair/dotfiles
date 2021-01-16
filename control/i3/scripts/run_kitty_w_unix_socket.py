#!/usr/bin/env python3

import subprocess as sp
import os

kitties_file = '/tmp/kitties'

try:
    with open(kitties_file, 'r') as kf:
        kitties = kf.readlines()
except: kitties = []

kitty_sockets = [ kitty.strip().split(';')[1] for kitty in kitties]

i = 1
while True:
    kitty_socket = 'unix:/tmp/kitty_s' + str(i)
    if kitty_socket not in kitty_sockets:
        this_kitty = sp.Popen(['/home/boris/kitty/kitty/launcher/kitty', '-o', 'allow_remote_control=yes', '--listen-on', kitty_socket], cwd='/home/boris')
        kitty_pid = str(this_kitty.pid)
        os.system(f"echo '{kitty_pid};{kitty_socket}' >> {kitties_file}")
        break
    i+=1

exit()
