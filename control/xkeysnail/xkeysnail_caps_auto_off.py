# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *
import os

def caps_lock_off():
    """Turn off caps lock"""
    os.system("/home/boris/bin/i3/caps-lock-off.sh &")

blacklist = [
    'pqiv_hint',
    'pqiv_hint_qtbrows',
    'devtools',
    'devtools_normal',
    'zenity_hjkl',
    'Python3',
    'Zotero',
    'Zotero_insert',
    'Zotero_float',
    'Zotero_float_insert',
]

define_keymap(lambda wm_class: wm_class not in blacklist, {
    K("ESC"): [K("ESC"), caps_lock_off],
    K("C-G"): [K("C-G"), caps_lock_off],
    K("C-C"): [K("C-C"), caps_lock_off],
    K("C-LEFT_BRACE"): [K("C-LEFT_BRACE"), caps_lock_off],
}, "caps_auto_off")

