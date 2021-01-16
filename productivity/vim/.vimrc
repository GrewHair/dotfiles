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

" return to normal mode and capslock off
imap JK <ESC>:silent exec "!/home/boris/bin/i3/caps-lock-off.sh" \| redraw!<CR>

nnoremap g. :

colo desert

call plug#begin('~/.vim/plugged')

Plug 'vim-scripts/AnsiEsc.vim'
Plug 'powerline/powerline'
Plug 'bpstahlman/txtfmt'
Plug 'liuchengxu/vim-which-key', { 'on': ['WhichKey', 'WhichKey!'] }

call plug#end()

" enable manpages - run :Man 3 printf
runtime! ftplugin/man.vim

let $PAGER=''
set modeline
set modelines=5

set mouse=a
