#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join
from random import choice

img_path = '/home/boris/.local/share/kitty/background_images/'
cfg_file = '/home/boris/projects/dotfiles/productivity/terminals/kitty/kitty.conf'

# Pick a random image from the images directory
img_files = [join(img_path, f) for f in listdir(img_path) if isfile(join(img_path, f))]
random_img_file = choice(img_files)

# Read the terminal's config file
with open(cfg_file, 'r') as cf:
    cfg_lines = cf.readlines()

# Change the last line to refer to the randomly picked image
cfg_lines[-1] = 'background_image ' + random_img_file + '\n'

# Write the result to the terminal's config file
with open(cfg_file, 'w') as cf:
    for cfg_line in cfg_lines:
        cf.write(cfg_line)
