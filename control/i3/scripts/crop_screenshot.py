#!/usr/bin/env python3
import os
from PIL import Image
import subprocess

# ---set the name of your (automatically numbered) screenshots (no extension)
imagename = "screenshot"
# ---set the path to where you (want to) save your screenshots
savepath = "/home/boris/cropped-screenshots"

def get(cmd):
    return subprocess.check_output(cmd).decode("utf-8")

n = 1 
while True:
    name = imagename+"_"+str(n)+".png"
    path = os.path.join(savepath, name)
    if os.path.exists(path):
        n += 1
    else:
        break

# make the shot
subprocess.call(["gnome-screenshot", "-f", path])
# get the width of the left screen
screenborder = [int(n) for n in [s for s in get("xrandr").split()\
                if "+0+0" in s][0].split("+")[0].split("x")]
# read the screenshot
im = Image.open(path)
width, height = im.size
# get the mouse position
mousepos = int(get(["xdotool", "getmouselocation"]).split()[0].split(":")[1])
top = 0
bottom = height

if mousepos <= screenborder[0]:
    left = 0
    right = screenborder[0]
else:
    left = screenborder[0]
    right = width
# create the image
im.crop((left, top, right, bottom)).save(os.path.join(savepath, "cropped_"+name))

