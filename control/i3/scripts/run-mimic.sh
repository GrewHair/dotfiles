#!/bin/bash
kill -9 $(ps -ef | grep 'mimic' | grep -v grep | grep -v run | awk '{print $2}')
cd /home/boris/mimic1/

if [ $# -ne 0 ]; then
    ./mimic -t "$*" -voice slt_hts &
else
    ./mimic -t "$(xsel -b | tr -d \#)" -voice slt_hts &
fi

# cd /home/boris/mimic1/
# ./mimic -t "$(xsel -b | tr -d \#)" -voice slt_hts &
exit 0
