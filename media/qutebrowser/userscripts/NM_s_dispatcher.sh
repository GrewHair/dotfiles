#!/bin/bash
if [[ $1:$2 == '127.0.0.1:8081' ]]
then
  echo '{"args":[":fake-key -g _d83tw"], "target_arg":"", "protocol_version":1}' | socat - UNIX-CONNECT:"${XDG_RUNTIME_DIR}/qutebrowser/ipc-$(echo -n "$USER" | md5sum | cut -d' ' -f1)"
else
  echo '{"args":[":fake-key -g ;"], "target_arg":"", "protocol_version":1}' | socat - UNIX-CONNECT:"${XDG_RUNTIME_DIR}/qutebrowser/ipc-$(echo -n "$USER" | md5sum | cut -d' ' -f1)"
fi
