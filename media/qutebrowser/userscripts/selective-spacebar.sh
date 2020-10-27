#!/bin/bash
if [[ $QUTE_URL == 'http://127.0.0.1:8081/' ]]
then
  echo "fake-key --global _dtw"  >> "$QUTE_FIFO"
else
  echo "fake-key <Space>" >> "$QUTE_FIFO"
fi
