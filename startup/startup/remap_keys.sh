#!/bin/sh -e

sleep 4

# Launch xkeysnail
#xhost +SI:localuser:root
#/home/boris/.local/bin/xkeysnail /home/boris/bin/xkeysnail-config.py
xkeysnail /home/boris/.config/xkeysnail/xkeysnail-config-builtin.py
# systemctl --user enable xkeysnail
# systemctl --user start xkeysnail

sleep 4

# Add (multipurpose) hyper modifier to the F3 button
# xmodmap -e 'clear mod3'
# xmodmap -e 'keycode 247 = F4'
# xmodmap -e 'keycode 70 = Hyper_R'
# xmodmap -e 'add mod3 = Hyper_R'
# xcape -e 'Hyper_R=F4'
xmodmap -e 'clear mod3'
xmodmap -e 'keycode 247 = F6'
xmodmap -e 'keycode 72 = Hyper_R'
xmodmap -e 'add mod3 = Hyper_R'
xcape -e 'Hyper_R=F6'

# fix things with xmodmap that xkeysnail can't handle
#xmodmap -e 'clear shift'
xmodmap -e 'keycode 94 = Shift_L'  # fix microsoft 4000 keyboard's weird key next to left shift
#xmodmap -e 'add shift = Shift_L'
xmodmap -e 'keycode 135 = Super_R' # turn microsoft 4000 keyboard's context menu button into the right super key

sleep 4

xset r rate 190 70

# disable key repeat for keys that are not (or not heavily) used for navigation
xset -r 65  # spacebar
xset -r 23  # tab
xset -r 49  # grave
xset -r 10  # key 1
xset -r 11  # key 2
xset -r 12  # key 3
xset -r 13  # key 4
xset -r 14  # key 5
xset -r 15  # key 6
xset -r 16  # key 7
xset -r 17  # key 8
xset -r 18  # key 9
xset -r 19  # key 0
xset -r 20  # minus
xset -r 21  # equals
xset -r 22  # backspace
xset -r 24  # q
# xset -r 25  # w
# xset -r 26  # e
xset -r 27  # r
xset -r 28  # t
# xset -r 29  # y
xset -r 30  # u
xset -r 31  # i
xset -r 32  # o
# xset -r 33  # p
xset -r 34  # opening square bracket
xset -r 35  # closing square bracket
xset -r 36  # enter
# xset -r 38  # a
# xset -r 39  # s
# xset -r 40  # d
# xset -r 41  # f
xset -r 42  # g
# xset -r 43  # h
# xset -r 44  # j
# xset -r 45  # k
# xset -r 46  # l
xset -r 47  # semicolon
xset -r 48  # apostrophe
xset -r 51  # backslash
xset -r 52  # z
# xset -r 53  # x
xset -r 54  # c
xset -r 55  # v
# xset -r 56  # b
# xset -r 57  # n
xset -r 58  # m
xset -r 59  # comma
xset -r 60  # period
xset -r 61  # forward slash


#xmodmap -e 'clear mod3'
#xmodmap -e 'keycode 247 = f'
#xmodmap -e 'keycode 41 = Hyper_R'
#xmodmap -e 'add mod3 = Hyper_R'
#xcape -e 'Hyper_R=f'

# Launch AutoKey (to bind hyper + [hjkl] to arrows)
#autokey-gtk &

exit 0
