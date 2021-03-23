# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *
import os
import subprocess as sp

def start_keynav():
    """Bypass xkeysnail and start keynav"""
    os.system("/home/boris/bin/i3/bypass-xkeysnail.py")
    os.system("keynav start,windowzoom &")

def close_devtools():
    """Unmark the browser window and close devtools"""
    os.system('i3-msg "[con_mark=inspect] mark --toggle inspect"')
    os.system('i3-msg "[con_id=__focused__] kill"')

def inspect():
    """Focus browser and launch keynav"""
    os.system('i3-msg [con_mark="inspect"] focus')
    os.system('keynav start,windowzoom &')

def set_wm_class_devtools():
    """Set WM_CLASS of the focused window to devtools"""
    os.system("xdotool set_window --class=devtools $(xdotool getactivewindow)")
    os.system("pkill conky")

def set_wm_class_devtools_insert():
    """Set WM_CLASS of the focused window to devtools_insert"""
    os.system("i3-msg split vertical")
    os.system("conky -t '-- INSERT --' &")
    os.system("xdotool set_window --class=devtools_insert $(xdotool getactivewindow)")

def set_wm_class_zotero():
    """Set WM_CLASS of the focused window to Zotero"""
    os.system("xdotool set_window --class=Zotero $(xdotool getactivewindow)")
    os.system("pkill conky")

def set_wm_class_zotero_insert():
    """Set WM_CLASS of the focused window to Zotero_insert"""
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
    K("N"): K("BTN_FORWARD"),
    K("P"): K("BTN_BACK"),
    K("I"): set_wm_class_devtools_insert,
    K("Shift-I"): [K("C-Shift-C"), inspect],
    K("SLASH"): [K("C-F"), set_wm_class_devtools_insert],
    K("Shift-SEMICOLON"): [K("C-Shift-p"), set_wm_class_devtools_insert],
    K("C"): start_keynav,
    K("X"): close_devtools,
    K("SPACE"): {
        K("SPACE"): [K("C-Shift-p"), set_wm_class_devtools_insert],
    },
}, "devtools_normal")

define_keymap(re.compile("^Zotero$|^Zotero_float$|^zenity_hjkl$|^Python3$|^devtools$"), {
    K("J"): K("DOWN"),
    K("K"): K("UP"),
    K("L"): K("RIGHT"),
    K("H"): K("LEFT"),
    K("G"): K("HOME"),
    K("Shift-G"): K("END"),
    K("C-G"): K("ESC"),
    K("C-C"): K("ESC"),
    # K("C-LEFT_BRACE"): K("ESC"),
}, "Vim normal mode bindings")

define_keymap(re.compile("^found.$"), {  # this window class is quite dangerous (because it's obscure)
    K("J"): K("DOWN"),
    K("K"): K("UP"),
    K("L"): K("RIGHT"),
    K("H"): K("LEFT"),
    K("C-J"): [K("DOWN")]*50,
    K("C-K"): [K("UP")]*50,
    K("C-L"): [K("RIGHT")]*50,
    K("C-H"): [K("LEFT")]*50,
    K("EQUAL"): K("Shift-EQUAL"),
}, "Vim navigation for xzoom")

define_keymap(re.compile("^Zotero$|^Zotero_float$|^zenity_hjkl$|^Python3$"), {
    K("C-J"): K("C-DOWN"),
    K("C-K"): K("C-UP"),
    K("C-L"): K("C-RIGHT"),
    K("C-H"): K("C-LEFT"),
    K("C-T"): K("C-SPACE"),
    K("Shift-J"): K("Shift-DOWN"),
    K("Shift-K"): K("Shift-UP"),
    K("Shift-L"): K("Shift-RIGHT"),
    K("Shift-H"): K("Shift-LEFT"),
    K("C-LEFT_BRACE"): K("ESC"),
}, "multicursor thing for Vim normal mode bindings")

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

define_keymap(re.compile("Zotero|^zenity_hjkl|devtools|VirtualBox|Manager|Machine"), {
    K("C-I"): K("TAB"),
    K("C-M-I"): K("Shift-TAB"),
    K("C-n"): K("DOWN"),
    K("C-p"): K("UP"),
    K("M-e"): K("C-END"),
    K("M-a"): K("C-HOME"),
    K("C-j"): K("ENTER"),
    K("C-m"): K("ENTER"),
}, "terminal-style bindings")

define_keymap(re.compile("^Gitter$"), {
    K("C-I"): K("TAB"),
    K("C-M-I"): K("Shift-TAB"),
    K("C-n"): K("PAGE_DOWN"),
    K("C-p"): K("PAGE_UP"),
    K("C-j"): K("ENTER"),
    K("C-m"): K("ENTER"),
    K("C-g"): K("ESC"),
    K("C-Shift-SLASH"): K("C-M-Shift-M"),  # markdown help
    K("C-O"): K("C-M-Shift-C"),  # focus chat input
}, "gitter bindings")

define_keymap(re.compile("devtools"), {
    K("C-f"): K("RIGHT"),
    K("C-b"): K("LEFT"),
    K("M-f"): K("C-RIGHT"),
    K("M-b"): K("C-LEFT"),
    K("C-e"): K("END"),
    K("C-a"): K("HOME"),
    K("C-h"): K("BACKSPACE"),
    K("C-w"): K("C-BACKSPACE"),
    K("C-u"): [K("Shift-HOME"), K("DELETE")],
    K("C-d"): K("DELETE"),
    K("C-k"): [K("Shift-END"), K("DELETE")],
}, "Readline-style bindings for devtools and qt apps")

define_keymap(re.compile("Manager|VirtualBox|Machine"), {
    K("C-f"): K("RIGHT"),
    K("C-b"): K("LEFT"),
    K("C-e"): K("END"),
    K("C-a"): K("HOME"),
    K("C-h"): K("BACKSPACE"),
    K("C-w"): K("C-BACKSPACE"),
    K("C-u"): [K("Shift-HOME"), K("DELETE")],
    K("C-d"): K("DELETE"),
    K("C-k"): [K("Shift-END"), K("DELETE")],
    K("C-g"): K("ESC"),
}, "Readline-style bindings for virtualbox")

define_keymap(re.compile("^Firefox$"), {
    K("C-w"): K("C-BACKSPACE"),
    K("C-n"): K("DOWN"),
    K("C-p"): K("UP"),
    K("C-j"): K("ENTER"),
    K("C-m"): K("ENTER"),
}, "Fix firefoxes inescapable shortcuts")

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

define_keymap(re.compile("^devtools_insert$"), {
    K("ESC"): set_wm_class_devtools,
    K("C-G"): set_wm_class_devtools,
    K("C-C"): set_wm_class_devtools,
    #K("C-LEFT_BRACE"): set_wm_class_devtools,
}, "devtools normal mode entry point")
