#!/bin/bash
keynav 'start,windowzoom,cut-up,cut-up,cut-left,cut-left,cut-right,warp,drag 1,windowzoom,cut-down,cut-down,cut-right,warp,click 1,end,sh "pkill keynav",sh "xdotool key ctrl+c && xsel -b | gvim -"'
# keynav 'start,windowzoom,cut-up,cut-up,cut-left,cut-left,cut-right,warp,drag 1,windowzoom,cut-down,cut-down,cut-right,warp,click 1,end,sh "pkill keynav"'
# xdotool key ctrl+c
# keynav 'start,windowzoom,click 1,end,sh "pkill keynav"'
# xsel -b | gvim -
