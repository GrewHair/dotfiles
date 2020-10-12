#!/bin/bash
echo "$QUTE_SELECTED_TEXT" | xsel -ib
echo "message-info 'Code yanked!'" >> "$QUTE_FIFO"
