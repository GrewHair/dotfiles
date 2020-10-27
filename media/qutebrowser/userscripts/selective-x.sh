#!/bin/bash
#echo "$QUTE_SELECTED_TEXT" | xsel -ib
#echo "message-info $QUTE_DATA_DIR" >> "$QUTE_FIFO"
if [[ $QUTE_URL != 'http://127.0.0.1:8081/' ]]
then
  echo "tab-close" >> "$QUTE_FIFO"
fi
