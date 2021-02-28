#!/bin/bash

# if [ -n $(as -aux | grep keynav | grep -v grep | grep -v start)]; then
#    pkill keynav
# fi

#pkill keynav || :

# this crap doesn't work!

keynav start,windowzoom &

exit 0
