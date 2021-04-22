#!/bin/bash


declare -A flags                    # flags to feed to tmux select-pane
flags[left]="-L"
flags[down]="-D"
flags[up]="-U"
flags[right]="-R"

declare -A step_out_criteria        # when to step out of tmux
step_out_criteria[left]='"#{pane_at_left}"'
step_out_criteria[down]='"#{pane_at_bottom}"'
step_out_criteria[up]='"#{pane_at_top}"'
step_out_criteria[right]='"#{pane_at_right}"'

declare -A find_closest_criteria    # when to step into tmux
find_closest_criteria[left]='"#{pane_at_right}"'
find_closest_criteria[down]='"#{pane_at_top}"'
find_closest_criteria[up]='"#{pane_at_bottom}"'
find_closest_criteria[right]='"#{pane_at_left}"'



function get_win_props {
    win_id=$(xdotool getactivewindow)
    win_class=$(xprop WM_CLASS -id "${win_id}" | rev | cut -f2 -d\" | rev)
    tmux_client=$(grep -m1 "${win_id}" /tmp/tmux-clients | cut -d\; -f2)
}


function step_as_i3 {
    echo "stepping as i3"
    i3-msg focus "${direction}"
    get_win_props
    if [[ $win_class != kitty ]]; then
        return
    fi
    # at_edge="0"
    at_edge=$(tmux display-message -p -t "${tmux_client}" "${find_closest_criteria[$direction]}")
    until [[ "${at_edge}" == *"1"* ]]; do
        tmux select-pane -t "${tmux_client}" "${flag}"
        at_edge=$(tmux display-message -p -t "${tmux_client}" "${find_closest_criteria[$direction]}")
    done
}


function step_as_tmux {
    echo "stepping as tmux"
    if [[ "${at_edge}" == *"1"* ]]; then
        i3-msg focus "${direction}"
    else
        tmux select-pane -t "${tmux_client}" "${flag}"
    fi
}


direction=$1
get_win_props
flag="${flags[$direction]}"
at_edge=$(tmux display-message -p -t "${tmux_client}" "${step_out_criteria[$direction]}")


if [[ $win_class == kitty ]]; then
    step_as_tmux
else
    step_as_i3
fi


exit 0
