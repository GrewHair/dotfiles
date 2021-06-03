#!/bin/bash

if [ ! $(pgrep "spotifyd") ]; then
  /home/boris/spotifyd/target/release/spotifyd
fi

spt
