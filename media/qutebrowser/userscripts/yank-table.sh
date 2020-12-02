#!/bin/bash
echo "$QUTE_SELECTED_HTML" | xsel -ib
echo "message-info 'Table yanked!'" >> "$QUTE_FIFO"
