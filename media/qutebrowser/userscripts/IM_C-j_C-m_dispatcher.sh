#!/bin/bash
#xdotool key Return
echo '{"args":[":fake-key -g <Return>"], "target_arg":"", "protocol_version":1}' | socat - UNIX-CONNECT:"${XDG_RUNTIME_DIR}/qutebrowser/ipc-$(echo -n "$USER" | md5sum | cut -d' ' -f1)"

if [[ $1 == 'www.youtube.com' ]]
then
    xdotool key Escape
    echo '{"args":[":fake-key -g <Escape>"], "target_arg":"", "protocol_version":1}' | socat - UNIX-CONNECT:"${XDG_RUNTIME_DIR}/qutebrowser/ipc-$(echo -n "$USER" | md5sum | cut -d' ' -f1)"
fi
