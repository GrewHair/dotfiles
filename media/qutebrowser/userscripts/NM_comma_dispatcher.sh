#!/bin/bash
sleep 0.05  # we're having some race conditions here: sometimes xdotool types
            # too quickly and qutebrowser only sees the last two letters -
            # for example, in tiddlywiki it only sees tw - which opens a new
            # tiddlywiki tab; or on youtube it just sees yt - so it yanks the title
            # this sleep statement is an attempt to prevent this. I may need to
            # adjust the time tho :)

if [[ $1:$2 == '127.0.0.1:8081' ]]
then
  xdotool type _d44tw
elif [[ $1 == 'www.youtube.com' ]]
then
  xdotool type _d44yt
fi
