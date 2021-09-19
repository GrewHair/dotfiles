# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/home/boris/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="robbyrussell"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
	git
	zsh-autosuggestions
	pip
	node
	# zsh-syntax-highlighting
	fast-syntax-highlighting
	fzf
)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8


## Make tmux run by default (me)
if [[ ! $INSIDE_EMACS ]]; then
	#[[ $TERM != "screen" ]] && exec tmux
	[[ $TERM != "screen" ]] && exec tmux # && notify-send foo `tmux display-message -p "#{client-name}"`
	#notify-send foo `tmux display-message -p "#{client-name}"`
	#tmux display-message -p "#{client-name}"
fi

# kitty integration
# it significantly slows down loading - so commenting out
#autoload -Uz compinit
#compinit
## Completion for kitty
#kitty + complete setup zsh | source /dev/stdin

# Enable powerline (me)
function powerline_precmd() {
    PS1="$(powerline-shell --shell zsh $?)"
}

function install_powerline_precmd() {
  for s in "${precmd_functions[@]}"; do
    if [ "$s" = "powerline_precmd" ]; then
      return
    fi
  done
  precmd_functions+=(powerline_precmd)
}

if [ "$TERM" != "linux" ]; then
    install_powerline_precmd
fi


# Call Neofetch at startup and clear (but not in Emacs) (me)
if [[ ! $INSIDE_EMACS ]]; then
	neofetch
	alias clear="clear && neofetch"
fi


# Use vim as a man-page viewer (me)
export PAGER="/bin/sh -c \"unset PAGER;col -b -x | \
    vim -R -c 'set ft=man nomod nolist' -c 'map q :q<CR>' \
    -c 'map <SPACE> <C-D>' -c 'map b <C-U>' \
    -c 'nmap K :Man <C-R>=expand(\\\"<cword>\\\")<CR><CR>' -\""

# Make fzf see hidden files
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"

# go
export GOPATH=$HOME/go
export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin

export EDITOR=vim

#ZSH_HIGHLIGHT_STYLES[comment]=grey

# disable C-s so it won't hang the terminal (in vim for example)
stty stop undef
stty start undef

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
alias sudo="sudo "
alias usdo="sudo "
alias im="/home/boris/bin/i3/set_terminal_background_image.sh"
alias ls=lsd
alias less="vim -R -c 'nmap q ZQ'"
alias vifm="tmux rename-session vifm && vifm"
alias htop="tmux rename-session htop && htop"
alias stig="tmux rename-session stig && stig"
alias sc-im="tmux rename-session sc-im && sc-im"
alias browsh="tmux rename-session browsh && browsh"
alias tuir="tmux rename-session tuir && tuir"
alias tm="tmux list-keys -T prefix | sed 's/.*prefix\s//g' | grep -v display-menu | vim -c 'set nornu | set syntax=tmux | nmap q :qa!<CR> | execute Columns()' -"
alias tc="tmux list-keys -T copy-mode | sed 's/.*copy-mode\s//g' | vim -c 'set nornu | set syntax=tmux | nmap q :qa!<CR> | execute Columns()' -"
alias xs="xsel -b"
alias startvenv="source ./venv/bin/activate"

# this is a crutch I'll use until I learn how to
# properly install self-compiled C programs
alias picoc="/home/boris/picoc/picoc"

# typo aliases :)
alias celar="clear"
alias clera="clear"
alias cler="clear"
alias clare="clear"
alias elss="less"

alias vmi="vim"
alias ivm="vim"

alias og="go"

alias pt="apt"
alias at="apt"
alias mn="man"

alias grpe="grep"
alias eixt="exit"
alias exti="exit"

alias pytohn3 python3

alias poewroff="poweroff"

alias ehco="echo"

alias ocnvert convert
alias tessearct="tesseract"

# key rebinds
# make C-P C-N scroll actual history (so I can quickly skip history with preceding space)
#bindkey -r "^N"
#bindkey "^N" history-search-forward
#bindkey "^N" history-beginning-search-forward
#bindkey -r "^P"
#bindkey "^P" history-search-backward
#bindkey "^P" history-beginning-search-backward

# attempt to associate win id with tmux client tty (to merge i3 and tmux navigation
if [[ `xprop WM_CLASS -id $(xdotool getactivewindow) | rev | cut -f2 -d\" | rev` == kitty ]]; then
    sed -i /$(xdotool getactivewindow)/d /tmp/tmux-clients &> /dev/null
    echo "`xdotool getactivewindow`;`tmux display-message -p '#{client_name}'`" >> /tmp/tmux-clients
fi
