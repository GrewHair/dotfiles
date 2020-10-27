#!/bin/bash
if [[ $1 == 'http://127.0.0.1:8081/' ]]
then
  # qutebrowser ':fake-key --global _dtw'
  # xdotool key underscore
  # xdotool key d
  # xdotool key t
  # xdotool key w
  xdotool type _dtw
  # echo "fake-key --global _dtw"  >> "$QUTE_FIFO"
else
  xdotool key space
  # qutebrowser ':fake-key --global <Space>'
  # echo "fake-key <Space>" >> "$QUTE_FIFO"
fi
