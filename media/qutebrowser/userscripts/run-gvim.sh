#!/bin/bash
echo "$QUTE_SELECTED_TEXT" | gvim - -c 'nmap j gjh | vmap j gjh | nmap k gkh | vmap k gkh | nmap q ZQ | vmap q <ESC>ZQ | nmap x ZQ | vmap x <ESC>ZQ | nmap i ZQ | vmap i <ESC>ZQ | nmap o ZQ | nmap s ZQ | vmap s gs | nmap d ZQ | vmap d <ESC>ZQ | nmap c ZQ | vmap c <ESC>ZQ | nmap n ZQ | vmap n <ESC>ZQ |'
exit 0
