#!/bin/bash
kill -9 $(ps -ef | grep 'mimic' | grep -v grep | grep -v run | awk '{print $2}')
# pkill mimic
#echo $(echo "search $QUTE_SELECTED_TEXT" | tr '\r\n' ' ') >> "$QUTE_FIFO"
echo "search $QUTE_SELECTED_TEXT" >> "$QUTE_FIFO"
echo clear-messages >> "$QUTE_FIFO"
#echo "search $QUTE_SELECTED_TEXT" >> /tmp/mimic_script_log
cd /home/boris/mimic1/
./mimic -t "$QUTE_SELECTED_TEXT" -voice slt_hts &
#echo "=================" >> /tmp/mimic_script_log
exit 0
