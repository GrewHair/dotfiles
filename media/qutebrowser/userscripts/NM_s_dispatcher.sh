#!/bin/bash
#echo "$QUTE_SELECTED_TEXT" | xsel -ib
#echo "message-info $QUTE_DATA_DIR" >> "$QUTE_FIFO"
if [[ $1:$2 == '127.0.0.1:8081' ]]
then
  #xdotool type _d83tw
  echo '{"args":[":fake-key -g _d83tw"], "target_arg":"", "protocol_version":1}' | socat - UNIX-CONNECT:"${XDG_RUNTIME_DIR}/qutebrowser/ipc-$(echo -n "$USER" | md5sum | cut -d' ' -f1)"
else
  #xdotool key 47
  echo '{"args":[":fake-key -g ;"], "target_arg":"", "protocol_version":1}' | socat - UNIX-CONNECT:"${XDG_RUNTIME_DIR}/qutebrowser/ipc-$(echo -n "$USER" | md5sum | cut -d' ' -f1)"
fi
