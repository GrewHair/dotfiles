#!/bin/bash
state=$(cat /tmp/qutebrowser-keydrown)

if [ "$state" == "off" ]; then
    echo "message-info 'keydrown on'" >> "$QUTE_FIFO"
    echo "unbind j" >> "$QUTE_FIFO"
    echo "unbind j" >> "$QUTE_FIFO"
    echo "unbind k" >> "$QUTE_FIFO"
    echo "unbind k" >> "$QUTE_FIFO"
    echo "unbind e" >> "$QUTE_FIFO"
    echo "unbind e" >> "$QUTE_FIFO"
    echo "unbind d" >> "$QUTE_FIFO"
    echo "unbind d" >> "$QUTE_FIFO"
    echo "unbind --mode caret e" >> "$QUTE_FIFO"
    echo "unbind --mode caret e" >> "$QUTE_FIFO"
    echo "unbind --mode caret d" >> "$QUTE_FIFO"
    echo "unbind --mode caret d" >> "$QUTE_FIFO"
    echo "on" > /tmp/qutebrowser-keydrown
else
    echo "message-info 'keydrown off'" >> "$QUTE_FIFO"
    echo "bind j scroll down" >> "$QUTE_FIFO"
    echo "bind j scroll down" >> "$QUTE_FIFO"
    echo "bind k scroll up" >> "$QUTE_FIFO"
    echo "bind k scroll up" >> "$QUTE_FIFO"
    echo "bind e scroll-page 0 -0.1" >> "$QUTE_FIFO"
    echo "bind e scroll-page 0 -0.1" >> "$QUTE_FIFO"
    echo "bind d scroll-page 0 0.1" >> "$QUTE_FIFO"
    echo "bind d scroll-page 0 0.1" >> "$QUTE_FIFO"
    echo "bind --mode caret e scroll-page 0 -0.1" >> "$QUTE_FIFO"
    echo "bind --mode caret e scroll-page 0 -0.1" >> "$QUTE_FIFO"
    echo "bind --mode caret d scroll-page 0 0.1" >> "$QUTE_FIFO"
    echo "bind --mode caret d scroll-page 0 0.1" >> "$QUTE_FIFO"
    echo "off" > /tmp/qutebrowser-keydrown
fi

exit 0
