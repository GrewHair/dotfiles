#!/bin/bash

kill -9 $(ps -ef | grep 'RHVoice-client' | grep -v grep | grep -v run | awk '{print $2}')

echo "search $QUTE_SELECTED_TEXT" >> "$QUTE_FIFO"
echo clear-messages >> "$QUTE_FIFO"
echo "$QUTE_SELECTED_TEXT" | RHVoice-client -s Anna+CLS | aplay --disable-softvol
exit 0
