#!/bin/bash

if [[ $1 =~ .*youtu.* ]]; then
    qutebrowser --basedir /home/boris/qutebrowser-profiles/youtube --qt-arg name mpv $1 &
else
    qutebrowser $1 &

exit 0
