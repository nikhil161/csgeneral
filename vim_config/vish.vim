" local syntax file - set colors on a per-machine basis:
" vim: tw=0 ts=4 sw=4
" Vim color file
" Maintainer:	Vishal Prasad
" Last Change:	2017 October 21

set background=dark
hi clear
if exists("syntax_on")
  syntax reset
endif
let g:colors_name = "ron"
hi Normal		guifg=PaleTurquoise4	guibg=black
hi NonText		guifg=brown
hi comment		guifg=coral
hi constant		guifg=#a8a8a8	gui=bold
hi identifier	guifg=cyan	gui=NONE
hi statement	guifg=lightblue	gui=NONE
hi preproc		guifg=Pink2
hi type			guifg=seagreen	gui=bold
hi special		guifg=yellow
hi ErrorMsg		guifg=Black	guibg=Red
hi WarningMsg	guifg=Black	guibg=Green
hi Error		guibg=Red
hi Todo			guifg=Black	guibg=orange
hi Cursor		guibg=#60a060 guifg=#00ff00
hi Search		guibg=lightslateblue
hi IncSearch	gui=NONE guibg=steelblue
hi LineNr		guifg=darkgrey
hi title		guifg=darkgrey
hi StatusLineNC	gui=NONE guifg=lightblue guibg=darkblue
hi StatusLine	gui=bold	guifg=cyan	guibg=blue
hi label		guifg=gold2
hi operator		guifg=orange
hi clear Visual
hi Visual		term=reverse cterm=reverse gui=reverse
hi DiffChange   guibg=darkgreen
hi DiffText		guibg=olivedrab
hi DiffAdd		guibg=slateblue
hi DiffDelete   guibg=coral
hi Folded		guibg=gray30
hi FoldColumn	guibg=gray30 guifg=white
hi cIf0			guifg=gray