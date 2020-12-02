#!/bin/bash
kill -9 $(ps -ef | grep 'mimic' | grep -v grep | grep -v run | awk '{print $2}')
cd /home/boris/mimic1/
./mimic -t "$QUTE_SELECTED_TEXT" -voice slt_hts &
exit 0
