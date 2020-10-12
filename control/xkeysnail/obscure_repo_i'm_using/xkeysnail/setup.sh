#!/bin/bash

PWD=$(pwd)
echo $PWD
sudo ln -s $PWD/xkeysnail.service $HOME/.config/systemd/user/xkeysnail.service
sudo cp $PWD/10-input.rules /etc/udev/rules.d/10-input.rules
sudo cp $PWD/10-uinput.rules /etc/udev/rules.d/10-uinput.rules


