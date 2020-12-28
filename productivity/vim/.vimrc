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
inoremap kj <Esc>
inoremap j9 6
inoremap jv ^
inoremap j/ \
inoremap f9 6
inoremap fv ^
inoremap f/ \

inoremap ji │
inoremap je ├
inoremap j- ─
inoremap jl └
inoremap jt ┬
inoremap fi │
inoremap fe ├
inoremap f- ─
inoremap fl └
inoremap ft ┬

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

nnoremap о j
nnoremap л k

colo desert

call plug#begin('~/.vim/plugged')

Plug 'vim-scripts/AnsiEsc.vim'

call plug#end()

" enable manpages - run :Man 3 printf
runtime! ftplugin/man.vim

let $PAGER=''
