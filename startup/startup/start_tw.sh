#!/bin/sh -e

sleep 2

# start tiddlywiki!
# tiddlywiki /home/boris/projects/tiddlywiki/wiki22 --server 8081 &
# tiddlywiki /home/boris/projects/tiddlywiki/wiki22 --listen port=8081 &
tiddlywiki /home/boris/projects/tiddlywiki/wiki22 --listen root-tiddler=$:/core/save/lazy-all port=8081 &
exit 0
