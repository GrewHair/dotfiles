#!/bin/bash
arr=($QUTE_SELECTED_TEXT)
echo "search ${arr[@]:0:3}" >> "$QUTE_FIFO"
echo "enter-mode caret" >> "$QUTE_FIFO"
