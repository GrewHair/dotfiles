#!/bin/bash

if [[ $QUTE_URL =~ .*watch.* ]]; then
    echo "fake-key f ;; spawn i3-msg fullscreen disable" >> "$QUTE_FIFO"
else
    echo "clear-messages ;; message-info web ;; hint links tab" >> "$QUTE_FIFO"
fi
