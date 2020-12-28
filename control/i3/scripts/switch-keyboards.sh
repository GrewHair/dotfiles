#!/bin/bash


function get_microsoft_ids()
{
    SAVEIFS=$IFS
    IFS=$'\n'
    microsoft_string=$(xinput list | grep Microsoft)
    microsoft_arr=($microsoft_string)
    IFS=$SAVEIFS
    
    microsoft_ids=()

    for (( i=0; i<${#microsoft_arr[@]}; i++ ))
    do
        microsoft_ids[i]=$(echo ${microsoft_arr[$i]} | grep -P '(?<=id=)\d+' -o)
    done
}


function get_builtin_id()
{
    builtin_id=$(xinput list | grep 'AT Translated Set' | grep -P '(?<=id=)\d+' -o)
}


function enable_microsoft()
{
    for (( i=0; i<${#microsoft_ids[@]}; i++ ))
    do
        xinput enable ${microsoft_ids[$i]}
    done
}


function disable_microsoft()
{
    for (( i=0; i<${#microsoft_ids[@]}; i++ ))
    do
        xinput disable ${microsoft_ids[$i]}
    done
}


function enable_builtin()
{
    xinput enable $builtin_id
}


function disable_builtin()
{
    xinput disable $builtin_id
}


function get_microsoft_handler()
{
    microsoft_handler=$(cat /proc/bus/input/devices | awk -v RS='' '/Microsoft/' | grep Handlers | grep -P 'event[0-9]*' -o -m 1)
}

function get_builtin_handler()
{
    builtin_handler=$(cat /proc/bus/input/devices | awk -v RS='' '/AT Translated Set/' | grep Handlers | grep -P 'event[0-9]*' -o)
}


function kill_xkeysnail()
{
    kill -9 $(ps -ef | grep 'xkeysnail' | grep -v grep | awk '{print $2}')
}


function start_xkeysnail()
{
    xkeysnail /home/boris/.config/xkeysnail/xkeysnail-config-"$1".py --devices /dev/input/$2 &
}


function toggle_touchpad()
{
    id=$(xinput list | grep Touchpad | grep -P '(?<=id=)\d+' -o)
    enabled=$(xinput --list-props $id | grep 'Device Enabled' | grep -P 1$ -o)
    if [[ $enabled ]]
    then
      xinput set-prop $id "Device Enabled" 0
    else
      xinput set-prop $id "Device Enabled" 1
    fi
}


function menu()
{
    which_keyboard=$(zenity --list --class=zenity_hjkl --column Keyboard Builtin Microsoft 'Toggle touchpad' Lock)
}


menu
get_microsoft_ids
get_builtin_id
get_microsoft_handler
get_builtin_handler

if [[ $which_keyboard ==  Builtin ]]; then
    kill_xkeysnail
    enable_builtin
    disable_microsoft
    start_xkeysnail builtin $builtin_handler
fi

if [[ $which_keyboard ==  Microsoft ]]; then
    kill_xkeysnail
    enable_microsoft
    disable_builtin
    start_xkeysnail microsoft $microsoft_handler
fi

if [[ $which_keyboard == 'Toggle touchpad' ]]; then
    toggle_touchpad
fi

exit 0
