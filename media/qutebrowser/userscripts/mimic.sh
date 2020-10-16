#!/bin/bash
kill -9 $(ps -ef | grep 'mimic' | grep -v grep | grep -v stop |  awk '{print $2}')
echo "search $QUTE_SELECTED_TEXT" >> "$QUTE_FIFO"
cd /home/boris/mimic1/
./mimic -t "$QUTE_SELECTED_TEXT" -voice slt_hts
