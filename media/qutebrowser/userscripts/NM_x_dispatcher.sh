#!/bin/bash
#echo "$QUTE_SELECTED_TEXT" | xsel -ib
#echo "message-info $QUTE_DATA_DIR" >> "$QUTE_FIFO"
if [[ $1:$2 == '127.0.0.1:8081' ]]
then
  #xdotool type _d88tw
  echo '{"args":[":fake-key -g _d88tw"], "target_arg":"", "protocol_version":1}' | socat - UNIX-CONNECT:"${XDG_RUNTIME_DIR}/qutebrowser/ipc-$(echo -n "$USER" | md5sum | cut -d' ' -f1)"
else
  #xdotool type _d88al
  echo '{"args":[":fake-key -g _d88al"], "target_arg":"", "protocol_version":1}' | socat - UNIX-CONNECT:"${XDG_RUNTIME_DIR}/qutebrowser/ipc-$(echo -n "$USER" | md5sum | cut -d' ' -f1)"
fi
