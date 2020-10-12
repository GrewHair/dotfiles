#!/usr/bin/python3

import os
devnode = '/dev/uinput'
result = os.access(devnode, os.W_OK)
print("Access: {}".format(result))
