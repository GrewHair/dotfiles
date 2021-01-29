# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *
import os
import subprocess as sp

def set_opacity_lo():
    """Set window opacity to a low value"""
    os.system("compton-trans -c 15")

def set_opacity_hi():
    """Set window opacity to a high value"""
    os.system("compton-trans -c 100")

hint_handlers = []

for i in range(30):
    def hint_handler(i=i):
        os.system('pkill mimic')
        os.system('pkill gvim')
        str_num = str(i+1)
        get_addr_cmd = f"cat /tmp/hint-data | grep ^3 | sed -n '{str_num}p' | cut -f3,4"
        addr = sp.check_output(get_addr_cmd, shell=True, text=True).strip().split('\t')
        get_text_cmd = f"cat /tmp/hint-data | grep -P '^5\t[0-9]*\t{addr[0]}\t{addr[1]}' | cut -f12 | paste -sd ' ' -"
        text = sp.check_output(get_text_cmd, shell=True, text=True)
        os.system('echo "' + text + '" > /tmp/hint-text')
        os.system('cd /home/boris/mimic1 && ./mimic -t "' + text + '" -voice slt_hts &')
        # this almost works, except for one thing: gvim starts at an unpredictable workspace
        try:
            launch_gvim = sp.check_output('cat /tmp/launch_gvim', shell=True, text=True).strip()
        except:
            launch_gvim = 'yes'
        if launch_gvim == 'yes':
            os.system("gvim /tmp/hint-text --class=gvim_zathura -c 'nmap j gjh | vmap j gjh | nmap k gkh | vmap k gkh | nmap q ZQ | vmap q <ESC>ZQ | nmap x ZQ | vmap x <ESC>ZQ | nmap i ZQ | vmap i <ESC>ZQ | nmap o ZQ | nmap s ZQ | vmap s gs | nmap d ZQ | vmap d <ESC>ZQ | nmap c ZQ | vmap c <ESC>ZQ | nmap n ZQ | vmap n <ESC>ZQ | nmap m ZQ | vmap m <ESC>ZQ'")

    hint_handlers.append(hint_handler)

hint_qutebrowser_handlers = []

for i in range(30):
    def hint_qutebrowser_handler(i=i):
        os.system('pkill mimic')
        str_num = str(i+1)
        get_addr_cmd = f"cat /tmp/hint-data | grep ^3 | sed -n '{str_num}p' | cut -f3,4"
        addr = sp.check_output(get_addr_cmd, shell=True, text=True).strip().split('\t')
        get_text_cmd = f"cat /tmp/hint-data | grep -P '^5\t[0-9]*\t{addr[0]}\t{addr[1]}' | cut -f12 | paste -sd ' ' -"
        text = sp.check_output(get_text_cmd, shell=True, text=True)
        os.system('echo "' + text + '" > /tmp/hint-text')
        os.system('cd /home/boris/mimic1 && ./mimic -t "' + text + '" -voice slt_hts &')
        os.system('pkill pqiv')

    hint_qutebrowser_handlers.append(hint_qutebrowser_handler)


define_keymap(re.compile("^pqiv_hint$"), {
    K("Q"): hint_handlers[0],
    K("W"): hint_handlers[1],
    K("E"): hint_handlers[2],
    K("R"): hint_handlers[3],
    K("T"): hint_handlers[4],
    K("Y"): hint_handlers[5],
    K("U"): hint_handlers[6],
    K("I"): hint_handlers[7],
    K("O"): hint_handlers[8],
    K("P"): hint_handlers[9],
    K("LEFT_BRACE"): hint_handlers[10],
    K("RIGHT_BRACE"): hint_handlers[11],
    K("A"): hint_handlers[12],
    K("S"): hint_handlers[13],
    K("D"): hint_handlers[14],
    K("F"): hint_handlers[15],
    K("G"): hint_handlers[16],
    K("H"): hint_handlers[17],
    K("J"): hint_handlers[18],
    K("K"): hint_handlers[19],
    K("L"): hint_handlers[20],
    K("SEMICOLON"): hint_handlers[21],
    K("Z"): hint_handlers[22],
    K("X"): hint_handlers[23],
    K("C"): hint_handlers[24],
    K("V"): hint_handlers[25],
    K("B"): hint_handlers[26],
    K("N"): hint_handlers[27],
    K("M"): hint_handlers[28],
    K("SLASH"): hint_handlers[29],
    K("C-r"): K("N"),
    K("C-g"): K("Q"),
    K("C-c"): K("Q"),
    K("C-LEFT_BRACE"): K("Q"),
    K("ESC"): K("Q"),
    K("C-LEFT_BRACE"): set_opacity_lo,
    K("C-RIGHT_BRACE"): set_opacity_hi,
}, "pqiv_hint")

define_keymap(re.compile("pqiv_hint_qtbrows"), {
    K("Q"): hint_qutebrowser_handlers[0],
    K("W"): hint_qutebrowser_handlers[1],
    K("E"): hint_qutebrowser_handlers[2],
    K("R"): hint_qutebrowser_handlers[3],
    K("T"): hint_qutebrowser_handlers[4],
    K("Y"): hint_qutebrowser_handlers[5],
    K("U"): hint_qutebrowser_handlers[6],
    K("I"): hint_qutebrowser_handlers[7],
    K("O"): hint_qutebrowser_handlers[8],
    K("P"): hint_qutebrowser_handlers[9],
    K("LEFT_BRACE"): hint_qutebrowser_handlers[10],
    K("RIGHT_BRACE"): hint_qutebrowser_handlers[11],
    K("A"): hint_qutebrowser_handlers[12],
    K("S"): hint_qutebrowser_handlers[13],
    K("D"): hint_qutebrowser_handlers[14],
    K("F"): hint_qutebrowser_handlers[15],
    K("G"): hint_qutebrowser_handlers[16],
    K("H"): hint_qutebrowser_handlers[17],
    K("J"): hint_qutebrowser_handlers[18],
    K("K"): hint_qutebrowser_handlers[19],
    K("L"): hint_qutebrowser_handlers[20],
    K("SEMICOLON"): hint_qutebrowser_handlers[21],
    K("Z"): hint_qutebrowser_handlers[22],
    K("X"): hint_qutebrowser_handlers[23],
    K("C"): hint_qutebrowser_handlers[24],
    K("V"): hint_qutebrowser_handlers[25],
    K("B"): hint_qutebrowser_handlers[26],
    K("N"): hint_qutebrowser_handlers[27],
    K("M"): hint_qutebrowser_handlers[28],
    K("SLASH"): hint_qutebrowser_handlers[29],
    K("C-r"): K("N"),
    K("C-g"): K("Q"),
    K("C-c"): K("Q"),
    K("C-LEFT_BRACE"): K("Q"),
    K("ESC"): K("Q"),
    K("C-LEFT_BRACE"): set_opacity_lo,
    K("C-RIGHT_BRACE"): set_opacity_hi,
}, "pqiv_hint_qutebrowser")
