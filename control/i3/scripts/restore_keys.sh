#!/bin/sh -e

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

xset -r 65
xset -r 23

exit 0
