# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    Key.CAPSLOCK: Key.LEFT_CTRL,
    # Key.LEFT_META: Key.LEFT_CTRL,
    # Key.LEFT_CTRL: Key.LEFT_META,
    Key.LEFT_CTRL: Key.LEFT_META,
    Key.LEFT_META: Key.LEFT_ALT,
    Key.LEFT_ALT: Key.LEFT_CTRL,
    Key.RIGHT_META: Key.HENKAN
})

define_multipurpose_modmap({
})

"""
define_keymap(None, {
    K('C-h'): Key.Left
}, "test")
"""
