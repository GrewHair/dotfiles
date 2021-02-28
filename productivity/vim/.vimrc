set keymap=russian-jcukenwin
set iminsert=0
set imsearch=0
highlight lCursor guifg=NONE guibg=Cyan


set nu rnu
set hlsearch
set cursorline
set clipboard=unnamedplus
set t_Co=256


inoremap jk <Esc>
inoremap 99 6
inoremap vv ^

" inoremap ji │
" inoremap je ├
" inoremap j- ─
" inoremap jl └
" inoremap jt ┬
" inoremap fi │
" inoremap fe ├
" inoremap f- ─
" inoremap fl └
" inoremap ft ┬

cnoremap jk <Esc>
cnoremap kj <Esc>
"cnoremap mm <Return>

"vnoremap jk <Esc>
"vnoremap kj <Esc>

" read selection
vmap gs y:silent exec "!/home/boris/bin/i3/run-mimic.sh" \| redraw!<CR>gv
vmap m y:silent exec "!/home/boris/bin/i3/run-mimic.sh" \| redraw!<CR>gv

" return to normal mode and capslock off
imap JK <ESC>:silent exec "!/home/boris/bin/i3/caps-lock-off.sh" \| redraw!<CR>

nnoremap g. :

" don't copy single characters when deleting
nnoremap x "_x
nnoremap X "_X
"colo desert

call plug#begin('~/.vim/plugged')

Plug 'vim-scripts/AnsiEsc.vim'
Plug 'powerline/powerline'
Plug 'bpstahlman/txtfmt'
Plug 'liuchengxu/vim-which-key', { 'on': ['WhichKey', 'WhichKey!'] }
Plug 'tmux-plugins/vim-tmux'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'airblabe/vim-rooter'
Plug 'liuchengxu/space-vim-dark'

call plug#end()

" enable manpages - run :Man 3 printf
runtime! ftplugin/man.vim

let $PAGER=''
set modeline
set modelines=5

set mouse=a
noremap <silent> \vs :<C-u>let @z=&so<CR>:set so=0 noscb<CR>:bo vs<CR>Ljzt:setl scb<CR><C-w>p:setl scb<CR>:let &so=@z<CR>
function Columns()
	execute "normal \\vs"
endfunction

"nnoremap <Space>j :check
"nnoremap <Space> :silent exec "!notify-send foo bar" \| redraw!<CR><Space>
"

colorscheme space-vim-dark
set termguicolors
let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"

