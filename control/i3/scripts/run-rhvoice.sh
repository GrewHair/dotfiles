#!/bin/bash
kill -9 $(ps -ef | grep 'RHVoice-client' | grep -v grep | grep -v run | awk '{print $2}')
xsel -b | RHVoice-client -s Anna+CLS | aplay --disable-softvol
exit 0
