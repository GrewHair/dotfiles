#!/usr/bin/env python3
import pyautogui
import cv2
import pytesseract
import subprocess as sp
from sys import argv

# target_output = argv[1]
# 
# get_ws_cmd = 'i3-msg -t get_workspaces'
# ws = json.loads(sp.run(get_ws_cmd, shell=True, stdout=sp.PIPE).stdout)
# #ws_masked = [{'name': w['name'], 'focused': w['focused'], 'output': w['output']} for w in ws]
# current_output = [w for w in ws if w['focused']][0]['output']
# 
# if current_output != target_output:
#     sp.run('i3-msg focus output ' + target_output, shell=True)
# else:
#     sp.run('i3-msg [workspace=shared] move workspace to output ' + target_output, shell=True)
#     sp.run('i3-msg workspace next_on_output', shell=True)

img = pyautogui.screenshot()
# img = cv2.imread(img)
data = pytesseract.image_to_data(img)
data_list = data.split('\n')
