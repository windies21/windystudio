Vim syntax and color highlighting 


~~~
$ cd
$ mkdir .vim
$ cd .vim
$ git clone https://github.com/sentientmachine/erics_vim_syntax_and_color_highlighting.git
$ mv erics_vim_syntax_and_color_highlighting/* .
$ rm -r erics_vim_syntax_and_color_highlighting 
$ git clone https://github.com/morhetz/gruvbox.git
$ cp -R gruvbox/* .
$ rm -r gruvbox
$ cd
$ vi .vimrc
~~~


.vimrc
~~~
autocmd BufRead,BufNewFile .{h,c,cpp} set cindent sw=4 sts=4   cino=:0,t0 ts=4 expandtab
autocmd BufRead,BufNewFile Makefile set sw=4 sts=4 cino=:0,t0 ts=4 noet
autocmd BufRead,BufNewFile .py set si sw=4 sts=4 ts=4 expandtab

syntax on
set incsearch
set hlsearch
set fencs=utf-8,euc-kr,ISO-8859-1,latin1
set path=/usr/include,/usr/local/include

"The following three lines map Ctrl+s to save in vi.  You can comment
"these out, it has nothing to do with syntax highlighting or colors.

" optional lines to turn on pressing F2 to toggle paste mode
noremap <F2> :set invpaste paste?<CR>i
set pastetoggle=<F2>


:nmap <c-s> :w<CR>
:imap <c-s> <Esc>:w<CR>a
:imap <c-s> <Esc><c-s>

syntax on
set background=light
set hlsearch
set nu
" set smartindent  "smartindent doesn't take care of python hashtag comments correctly, use cindent:
set cindent
set tabstop=4
set shiftwidth=4
set expandtab
"set cursorline"
filetype on
filetype plugin indent on

au BufReadPost,BufNewFile *.twig colorscheme koehler
au BufReadPost,BufNewFile *.css colorscheme slate
au BufReadPost,BufNewFile *.js colorscheme slate2
au BufReadPost,BufNewFile *.py colorscheme gruvbox
au BufReadPost,BufNewFile *.html colorscheme monokai
au BufReadPost,BufNewFile *.java colorscheme monokai
" au BufReadPost,BufNewFile *.php colorscheme monokai

" Default line highlighting for unknown filetypes
hi String ctermfg=140
hi CursorLine ctermbg=235
hi CursorLine guibg=#D3D3D3 cterm=none

"What follows are optional things, I like them

"au BufNewFile,BufRead *.py
"        \ set tabstop=4
"        \ set shiftwidth=4     "aand fedora doesn't like this parameter, remove this line.
"        \ set textwidth=79
"        \ set expandtab
"        \ set autoindent
"        \ set fileformat=unix

" Commenting blocks of code.
" This specifies the comment character when specifying block comments.
"autocmd FileType c,cpp,java,scala let b:comment_leader = '//'
"autocmd FileType sh,ruby,python   let b:comment_leader = '#'
"autocmd FileType conf,fstab       let b:comment_leader = '#'
"autocmd FileType tex              let b:comment_leader = '%'
"autocmd FileType mail             let b:comment_leader = '>'
"autocmd FileType vim              let b:comment_leader = '"'

"this makes it so you can Shift-V highlight lots of text then press ,cc to
"comment it or ,cu to uncomment.
"noremap <silent> ,cc :<C-B>silent <C-E>s/^/<C-R>=escape(b:comment_leader,'\/')<CR>/<CR>:nohlsearch<CR>
"noremap <silent> ,cu :<C-B>silent <C-E>s/^\V<C-R>=escape(b:comment_leader,'\/')<CR>//e<CR>:nohlsearch<CR>

"This mission critical workaround hack tells vim to restore cursor to the last line.
"Be sure to set: "Thip, crinkle, sploit" to "stopit, just be right".  lolz
"Also it could be the functionality is disabled in your /etc/vim/vimrc or
"your ~/.viminfo is owned by root.
"http://askubuntu.com/questions/223018/vim-is-not-remembering-last-position
autocmd BufReadPost *
  \ if line("'\"") > 1 && line("'\"") <= line("$") |
  \   exe "normal! g`\"" |
  \ endif

"These extra commands tell syntastic to ignore the following kinds of warnings
"let g:syntastic_quiet_messages = { "regex": 'superfluous' }
"let g:syntastic_quiet_messages = { "regex": 'superfluous-parens\|too-many-instance-attributes\|too-few-public-methods' }

"I like the vertical bar on insert mode, others do not like.  You decide.
"let &t_SI = "\<Esc>]50;CursorShape=1\x7" " Vertical bar in insert mode
"let &t_EI = "\<Esc>]50;CursorShape=0\x7" " Block in normal mode
~~~

Add this line to ~/.vim/colors/gruvbox.vim
~~~
let g:colors_name='gruvbox'
set background=dark             <-- this line
~~~


See.

[erics_vim_syntax_and_color_highlighting](https://github.com/sentientmachine/erics_vim_syntax_and_color_highlighting)

[gruvbox](https://github.com/morhetz/gruvbox)
