#!/bin/bash
if [[ $1:$2 == '127.0.0.1:8081' ]]
then
  xdotool type _d44tw
elif [[ $1 == 'www.youtube.com' ]]
then
  xdotool type _d44yt
fi
