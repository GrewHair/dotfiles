#!/bin/bash
#echo "$QUTE_SELECTED_TEXT" | xsel -ib
#echo "message-info $QUTE_DATA_DIR" >> "$QUTE_FIFO"
if [[ $1:$2 == '127.0.0.1:8081' ]]
then
  xdotool type _d83tw
else
  xdotool key 47
fi
