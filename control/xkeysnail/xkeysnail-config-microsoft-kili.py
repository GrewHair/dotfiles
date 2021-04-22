# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *
import os
import subprocess as sp
import importlib.util

# define timeout for multipurpose_modmap
define_timeout(0.3)

define_modmap(
    {
        Key.LEFT_META: Key.LEFT_SHIFT,
        # Key.LEFT_CTRL: Key.LEFT_META,
        Key.ESC: Key.RIGHT_META,
        # Key.RIGHT_CTRL: Key.RIGHT_META,
        # Key.LEFT_ALT: Key.LEFT_META,
        # Key.RIGHT_ALT: Key.RIGHT_META,
    }
)

define_multipurpose_modmap(
    {
        # Key.MENU: [Key.BLUETOOTH, Key.RIGHT_META],
        Key.LEFT_ALT: [Key.DOCUMENTS, Key.LEFT_META],
        Key.RIGHT_ALT: [Key.DOCUMENTS, Key.RIGHT_META],
        Key.SPACE: [Key.SPACE, Key.LEFT_CTRL],
        # Key.SPACE: [Key.BLUETOOTH, Key.LEFT_META],
        Key.ENTER: [Key.ENTER, Key.RIGHT_ALT],
        Key.CAPSLOCK: [Key.ESC, Key.LEFT_ALT],
        # Key.LEFT_CTRL: [Key.CAPSLOCK, Key.LEFT_CTRL],
        Key.SLASH: [Key.SLASH, Key.RIGHT_SHIFT],
        Key.DOT: [Key.DOT, Key.RIGHT_SHIFT],
        Key.COMMA: [Key.COMMA, Key.RIGHT_SHIFT],
        # Key.F2: [Key.F2, Key.LEFT_ALT],
        Key.F3: [Key.F3, Key.LEFT_ALT],
        Key.F4: [Key.F4, Key.LEFT_ALT],
        Key.F5: [Key.F5, Key.LEFT_ALT],
        Key.F7: [Key.F7, Key.RIGHT_ALT],
        Key.F8: [Key.F8, Key.RIGHT_ALT],
        Key.F9: [Key.F9, Key.RIGHT_ALT],
        Key.F10: [Key.F10, Key.RIGHT_ALT],
        Key.F11: [Key.F11, Key.RIGHT_ALT],
    }
)

define_keymap(re.compile('jetbrains-pycharm|jetbrains-idea'), {
    K("Shift-SPACE"): [K("COMMA"), K("SPACE")],
    K("C-COMMA"): [K("COMMA"), K("SPACE")],
}, "workaround for sticky multipurpose comma")

exec(open("/home/boris/.config/xkeysnail/xkeysnail_tts_hints.py").read())
exec(open("/home/boris/.config/xkeysnail/xkeysnail_modal_bindings.py").read())
exec(open("/home/boris/.config/xkeysnail/xkeysnail_caps_auto_off.py").read())

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
