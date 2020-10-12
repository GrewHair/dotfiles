#!/bin/sh -eu
c=$(stat -c%Z "$1")
find /etc /opt /usr -newerct @$(($c-${2:-10})) ! -newerct @$(($c+${2:-10})) ! -type d
