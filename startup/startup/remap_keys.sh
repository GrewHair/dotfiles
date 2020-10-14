#!/bin/sh -e

sleep 4

# Swap super and alt
#setxkbmap -option altwin:swap_alt_win

# Launch xkeysnail
#xhost +SI:localuser:root
#/home/boris/.local/bin/xkeysnail /home/boris/bin/xkeysnail-config.py
systemctl --user enable xkeysnail
systemctl --user start xkeysnail

sleep 4

# Add (multipurpose) hyper modifier to the F3 button
xmodmap -e 'clear mod3'
xmodmap -e 'keycode 247 = F3'
xmodmap -e 'keycode 69 = Hyper_R'
xmodmap -e 'add mod3 = Hyper_R'
xcape -e 'Hyper_R=F3'

#xmodmap -e 'clear shift'
xmodmap -e 'keycode 94 = Shift_L'
#xmodmap -e 'add shift = Shift_L'
xmodmap -e 'keycode 135 = Super_R'

xset r rate 175 70
xset -r 65
xset -r 23
#xmodmap -e 'clear mod3'
#xmodmap -e 'keycode 247 = f'
#xmodmap -e 'keycode 41 = Hyper_R'
#xmodmap -e 'add mod3 = Hyper_R'
#xcape -e 'Hyper_R=f'

# Launch AutoKey (to bind hyper + [hjkl] to arrows)
#autokey-gtk &

exit 0
