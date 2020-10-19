# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *
import os

#shift_pressed = False

def wheel_up():
    """Scroll the mousewheel up"""
    os.system('xdotool click 4')

def wheel_down():
    """Scroll the mousewheel down"""
    os.system('xdotool click 5')

def wheel_left():
    """Scroll the mousewheel left"""
    os.system('xdotool click 6')

def wheel_right():
    """Scroll the mousewheel right"""
    os.system('xdotool click 7')

def speak():
    """Speak selection"""
    os.system("kill -9 $(ps -ef | grep 'mimic' | grep -v grep | grep -v stop | awk '{print $2}')")
    os.system('cd /home/boris/mimic1 && xsel -p | mimic -voice slt_hts &')
    #os.system('xsel -p | mimic')
    #os.system('xsel -p | mimic -voice slt_hts')

def keydown_shift():
    """Depress shift button"""
    os.system('xdotool keydown shift')

def keyup_shift():
    """Release shift button"""
    os.system('xdotool keyup shift')

def keydown_ctrl():
    """Depress shift button"""
    os.system('xdotool keydown ctrl')

def keyup_ctrl():
    """Release shift button"""
    os.system('xdotool keyup ctrl')

def toggle_shift():  # wrong, i'll probably have to write a class
    """Toggle shift key"""
    global shift_pressed
    if shift_pressed:
        os.system('xdotool keyup ctrl')
        shift_pressed = False
    else:
        os.system('xdotool keydown ctrl')
        shift_pressed = True

# define timeout for multipurpose_modmap
define_timeout(0.3)

define_modmap(
    {
        Key.MENU: Key.RIGHT_META,
    }
)

define_multipurpose_modmap(
    {
        Key.LEFT_ALT: [Key.SPACE, Key.LEFT_CTRL],
        Key.RIGHT_ALT: [Key.SPACE, Key.RIGHT_CTRL],
        Key.ENTER: [Key.ENTER, Key.RIGHT_ALT],
        Key.BACKSLASH: [Key.BACKSLASH, Key.RIGHT_ALT],
        Key.CAPSLOCK: [Key.ESC, Key.LEFT_ALT],
        Key.LEFT_CTRL: [Key.CAPSLOCK, Key.LEFT_CTRL],
        Key.SLASH: [Key.SLASH, Key.RIGHT_SHIFT],
    }
)


define_keymap(re.compile("Vivaldi-stable"), {
    K("M-h"): K("LEFT"),
    K("M-j"): K("DOWN"),
    K("M-k"): K("UP"),
    K("M-l"): K("RIGHT"),
    K("M-Shift-h"): K("Shift-LEFT"),  # these 4 are for selection of text (since i can't replicate the true visual mode)
    K("M-Shift-j"): K("Shift-DOWN"),
    K("M-Shift-k"): K("Shift-UP"),
    K("M-Shift-l"): K("Shift-RIGHT"),
    K("M-C-j"): K("M-DOWN"),  # wtf are these two??
    K("M-C-k"): K("M-UP"),
    K("C-n"): K("DOWN"),
    K("C-p"): K("UP"),  # this binding does smth natively in devtools, but what it does is doubled by C-o
    K("C-f"): K("RIGHT"),  # fixed by the line below
    K("C-SLASH"): K("C-f"),
    K("C-b"): K("LEFT"), #!!!! sources
    K("M-f"): K("C-RIGHT"),
    K("M-b"): K("C-LEFT"),
    K("C-e"): K("END"),
    K("C-a"): K("HOME"),
    K("M-e"): K("C-END"),
    K("M-a"): K("C-HOME"),
    K("C-h"): K("BACKSPACE"),
    K("C-w"): K("C-BACKSPACE"),
    K("C-u"): [K("Shift-HOME"), K("DELETE")],
    K("C-d"): K("DELETE"),
    K("C-k"): [K("Shift-END"), K("DELETE")],
    K("C-j"): K("ENTER"),
    K("C-m"): K("ENTER"),
    K("M-w"): K("C-c"),
    K("C-w"): K("C-x"),
    K("C-y"): K("C-v"),
    K("M-TAB"): [K("TAB"), K("TAB")],
    K("M-Shift-TAB"): [K("Shift-TAB"), K("Shift-TAB")],
    K("C-SEMICOLON"): K("C-Shift-p"),
    K("M-v"): K("C-Shift-c"),
    K("C-m"): K("C-Shift-m"),
    K("M-n"): wheel_down,
    K("M-p"): wheel_up,
    K("M-y"): wheel_up,
}, "Vivaldi Devtools")

define_keymap(re.compile("figma-linux"), {
    K("M-h"): wheel_left,
    K("M-j"): wheel_down,
    K("M-k"): wheel_up,
    K("M-l"): wheel_right,
    K("C-y"): wheel_up,
    K("C-e"): wheel_down,
    K("C-SPACE"): K("C-BTN_MOUSE"),
    K("C-n"): K("DOWN"),
    K("C-p"): K("UP"),
    K("C-f"): K("RIGHT"),
    K("C-b"): K("LEFT"),
    K("M-f"): K("C-RIGHT"),
    K("M-b"): K("C-LEFT"),
    K("C-e"): K("END"),
    K("C-a"): K("HOME"),
    K("M-e"): K("C-END"),
    K("M-a"): K("C-HOME"),
    K("C-h"): K("BACKSPACE"),
    K("C-w"): K("C-BACKSPACE"),
    K("C-u"): [K("Shift-HOME"), K("DELETE")],
    K("C-d"): K("DELETE"),
    K("C-k"): [K("Shift-END"), K("DELETE")],
    K("C-j"): K("ENTER"),
    K("C-m"): K("ENTER"),
}, "Figma")

define_keymap(re.compile("Acroread"), {
    K("UP"): wheel_up,
    K("DOWN"): wheel_down,
    K("E"): wheel_up,
    K("D"): wheel_down,
    K("J"): K("DOWN"),
    K("K"): K("UP"),
    K("L"): K("RIGHT"),
    K("H"): K("LEFT"),
    K("KEY_0"): K("HOME"),
    K("Shift-J"): K("Shift-DOWN"),
    K("Shift-K"): K("Shift-UP"),
    K("Shift-L"): K("Shift-RIGHT"),
    K("Shift-H"): K("Shift-LEFT"),
    #K("B"): K("C-LEFT"),
    #K("W"): K("C-RIGHT"),
    #K("Shift-B"): K("C-Shift-LEFT"),
    #K("Shift-W"): K("C-Shift-RIGHT"),
    #K("Y"): [keydown_ctrl, K("C"), keyup_ctrl],
    K("S"): speak,
    K("V"): keydown_shift,
    # K("V"): toggle_shift,
    K("C"): keyup_shift,
}, "Acrobat Reader")

#define_multipurpose_modmap(
#    {Key.RIGHT_SHIFT: [Key.CAPSLOCK, Key.RIGHT_SHIFT]}
#)


# define_keymap(None, {K("C-e"): K("BTN_WHEEL")})

#os.system("xmodmap -e 'clear mod3'")
#os.system("xmodmap -e 'keycode 247 = F3'")
#os.system("xmodmap -e 'keycode 248 = Tab'")
#os.system("xmodmap -e 'keycode 69 = Hyper_R'")
#os.system("xmodmap -e 'keycode 23 = Hyper_L'")
#os.system("xmodmap -e 'add mod3 = Hyper_R'")
#os.system("xmodmap -e 'add mod3 = Hyper_L'")
#os.system("xcape -e 'Hyper_R=F3'")
#os.system("xcape -e 'Hyper_R=Tab'")
