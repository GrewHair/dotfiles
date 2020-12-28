#!/bin/bash
kill -9 $(ps -ef | grep 'mimic' | grep -v grep | grep -v run | awk '{print $2}')
# pkill mimic
echo "search $QUTE_SELECTED_TEXT" >> "$QUTE_FIFO"
cd /home/boris/mimic1/
./mimic -t "$QUTE_SELECTED_TEXT" -voice slt_hts &
exit 0
