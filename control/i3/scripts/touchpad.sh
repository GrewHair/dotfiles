#!/bin/bash

id=$(xinput list | grep Touchpad | grep -P '(?<=id=)\d+' -o)
enabled=$(xinput --list-props $id | grep 'Device Enabled' | grep -P 1$ -o)
if [[ $enabled ]]
then
  xinput set-prop $id "Device Enabled" 0
else
  xinput set-prop $id "Device Enabled" 1
fi
