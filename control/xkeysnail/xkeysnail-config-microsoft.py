# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *
import os
import subprocess as sp
import importlib.util
#spec = importlib.util.spec_from_file_location('xkeysnail_tts_hints', '/home/boris/.config/xkeysnail/xkeysnail_tts_hints.py')
#from xkeysnail_tts_hints import *
#from xkeysnail_modal_bindings import *

# define timeout for multipurpose_modmap
define_timeout(0.3)

# define_modmap(
#     {
#         Key.MENU: Key.RIGHT_META,
#     }
# )

# define_modmap(
#     {
#         Key.LEFT_META: Key.LEFT_SHIFT,
#     }
# )

define_multipurpose_modmap(
    {
        Key.MENU: [Key.BLUETOOTH, Key.RIGHT_META],
        Key.LEFT_ALT: [Key.SPACE, Key.LEFT_CTRL],
        Key.RIGHT_ALT: [Key.SPACE, Key.RIGHT_CTRL],
        # Key.SPACE: [Key.SPACE, Key.LEFT_CTRL],
        Key.SPACE: [Key.BLUETOOTH, Key.LEFT_META],
        Key.ENTER: [Key.ENTER, Key.RIGHT_ALT],
        # Key.BACKSLASH: [Key.BACKSLASH, Key.RIGHT_ALT],  # this only makes sense on the microsoft keyboard
        Key.CAPSLOCK: [Key.ESC, Key.LEFT_ALT],
        Key.LEFT_CTRL: [Key.CAPSLOCK, Key.LEFT_CTRL],
        Key.SLASH: [Key.SLASH, Key.RIGHT_SHIFT],
    }
)

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
