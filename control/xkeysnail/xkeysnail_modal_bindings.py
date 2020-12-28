# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *
import os
import subprocess as sp

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

def set_wm_class_devtools():
    """Set WM_CLASS of the focused window to devtools"""
    os.system("xdotool set_window --class=devtools $(xdotool getactivewindow)")

def set_wm_class_devtools_normal():
    """Set WM_CLASS of the focused window to devtools_normal"""
    os.system("xdotool set_window --class=devtools_normal $(xdotool getactivewindow)")

def set_wm_class_zotero():
    """Set WM_CLASS of the focused window to Zotero"""
    os.system("xdotool set_window --class=Zotero $(xdotool getactivewindow)")
    os.system("pkill conky")

def set_wm_class_zotero_insert():
    """Set WM_CLASS of the focused window to zotero_insert"""
    os.system("i3-msg split vertical")
    os.system("conky -t '-- INSERT --' &")
    os.system("xdotool set_window --class=Zotero_insert $(xdotool getactivewindow)")

def special_zotero_insert_tag():
    os.system("xdotool set_window --class=Zotero_insert $(xdotool getactivewindow)")
    os.system("i3-msg split vertical")
    os.system("conky -t '--INSERT --' &")
    os.system("sleep 0.2")
    os.system("xdotool key ctrl+alt+9")

def set_wm_class_zotero_float():
    """Set WM_CLASS of the focused window to Zotero_float"""
    os.system("sleep 0.1")
    os.system("xdotool set_window --class=Zotero_float $(xdotool getactivewindow)")
    os.system("pkill conky")

def set_wm_class_zotero_float_insert():
    """Set WM_CLASS of the focused window to zotero_insert"""
    os.system("xdotool set_window --class=Zotero_float_insert $(xdotool getactivewindow)")
    os.system("i3-msg split vertical")
    os.system("conky -c /home/boris/.config/conky/conky-insert_float.conf -t '-- INSERT --' &")


define_keymap(re.compile("^devtools$"), {
    K("M-h"): K("LEFT"),  # delete?
    K("M-j"): K("DOWN"),  # delete?
    K("M-k"): K("UP"),  # delete?
    K("M-l"): K("RIGHT"),  # delete?
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
    K("C-w"): K("C-x"),  #!!!!!
    K("C-y"): K("C-v"),
    K("M-TAB"): [K("TAB"), K("TAB")],
    K("M-Shift-TAB"): [K("Shift-TAB"), K("Shift-TAB")],
    K("C-SEMICOLON"): K("C-Shift-p"),
    K("M-v"): K("C-Shift-c"),
    K("C-m"): K("C-Shift-m"),
    K("M-n"): wheel_down,
    K("M-p"): wheel_up,
    K("M-y"): wheel_up,
    K("C-g"): set_wm_class_devtools_normal,
}, "devtools")

define_keymap(re.compile("devtools_normal"), {
    K("J"): K("DOWN"),
    K("K"): K("UP"),
    K("L"): K("RIGHT"),
    K("H"): K("LEFT"),
    K("I"): set_wm_class_devtools,
}, "devtools_normal")

define_keymap(re.compile("^Zotero$|^Zotero_float$|^zenity_hjkl$|^Python3$"), {
    K("J"): K("DOWN"),
    K("K"): K("UP"),
    K("L"): K("RIGHT"),
    K("H"): K("LEFT"),
    K("C-J"): K("C-DOWN"),
    K("C-K"): K("C-UP"),
    K("C-L"): K("C-RIGHT"),
    K("C-H"): K("C-LEFT"),
    K("C-T"): K("C-SPACE"),
    K("Shift-J"): K("Shift-DOWN"),
    K("Shift-K"): K("Shift-UP"),
    K("Shift-L"): K("Shift-RIGHT"),
    K("Shift-H"): K("Shift-LEFT"),
    K("G"): K("HOME"),
    K("Shift-G"): K("END"),
    K("C-G"): K("ESC"),
    K("C-C"): K("ESC"),
    K("C-LEFT_BRACE"): K("ESC"),
}, "Vim normal mode bindings + multicursor")

define_keymap(re.compile("^Zotero$"), {
    K("O"): K("F4"),
    K("D"): {
        K("C"): K("DELETE"),
        K("D"): K("Shift-DELETE"),
    },
    K("SPACE"): {
        K("KEY_2"): K("C-Shift-L"),
        K("KEY_3"): [K("C-T"), K("TAB"), K("TAB"),],
        K("KEY_7"): K("C-KEY_7"),
        K("KEY_8"): K("C-KEY_8"),
        K("KEY_9"): K("C-KEY_9"),
        K("KEY_0"): K("C-KEY_0"),
        K("A"): {
            K("S"): K("C-S"),
        },
        K("F"): {
            K("F"): [K("C-M-N"), K("UP"), K("UP"), K("ENTER"), set_wm_class_zotero_float],
        },
    },
    K("C"): {
        K("C"): K("F2"),
        K("KEY_7"): [ K("C-M-KEY_7"), set_wm_class_zotero_insert ],
        K("KEY_8"): [ K("C-M-KEY_8"), set_wm_class_zotero_insert ],
        K("KEY_9"): [ K("C-M-KEY_9"), set_wm_class_zotero_insert ],
        K("KEY_9"): special_zotero_insert_tag,
        K("KEY_0"): K("C-M-KEY_0"),
    },
    K("Q"): {
        K("Q"): K("C-W"),
    },
    K("SLASH"): [K("C-F"), set_wm_class_zotero_insert],
    K("I"): set_wm_class_zotero_insert,
}, "Spacemacs-style bindings for Zotero + insert mode entry point")

define_keymap(re.compile("^Zotero$|^Zotero_insert$"), {
    K("C-KEY_2"): [K("C-Shift-L"), set_wm_class_zotero],
    K("C-KEY_3"): [K("C-T"), K("TAB"), K("TAB"), set_wm_class_zotero],
}, "Focus Zotero's collections and items panes in both normal and insert modes")

define_keymap(re.compile("^Zotero_float$"), {
    K("SLASH"): [ K("C-F"), set_wm_class_zotero_float_insert],
    K("I"): set_wm_class_zotero_float_insert,
}, "Zotero floating insert mode entry point")

define_keymap(re.compile("Zotero|^zenity_hjkl$"), {
    K("C-I"): K("TAB"),
    K("C-M-I"): K("Shift-TAB"),
    K("C-n"): K("DOWN"),
    K("C-p"): K("UP"),
    # K("C-f"): K("RIGHT"),
    # K("C-b"): K("LEFT"),
    # K("M-f"): K("C-RIGHT"),
    # K("M-b"): K("C-LEFT"),
    # K("C-e"): K("END"),
    # K("C-a"): K("HOME"),
    K("M-e"): K("C-END"),
    K("M-a"): K("C-HOME"),
    # K("C-h"): K("BACKSPACE"),
    # K("C-w"): K("C-BACKSPACE"),
    # K("C-u"): [K("Shift-HOME"), K("DELETE")],
    # K("C-d"): K("DELETE"),
    # K("C-k"): [K("Shift-END"), K("DELETE")],
    K("C-j"): K("ENTER"),
    K("C-m"): K("ENTER"),
}, "Readline-style bindings for Zotero")

define_keymap(re.compile("^Zotero_float_insert$"), {
    K("ESC"): [K("ESC"), set_wm_class_zotero_float],
    K("C-G"): [K("ESC"), set_wm_class_zotero_float],
    K("C-C"): [K("ESC"), set_wm_class_zotero_float],
    K("C-LEFT_BRACE"): [K("ESC"), set_wm_class_zotero_float],
}, "Zotero floating normal mode entry point")

define_keymap(re.compile("^Zotero_insert$"), {
    K("ESC"): [K("ESC"), set_wm_class_zotero],
    K("C-G"): [K("ESC"), set_wm_class_zotero],
    K("C-C"): [K("ESC"), set_wm_class_zotero],
    K("C-LEFT_BRACE"): [K("ESC"), set_wm_class_zotero],
}, "Zotero normal mode entry point")
