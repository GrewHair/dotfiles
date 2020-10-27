// ==UserScript==
// @include	 http://127.0.0.1:8081/*
// ==/UserScript==

CodeMirror.Vim.map('jk', '<Esc>', 'insert')
CodeMirror.Vim.map('g.', ':', 'normal')

CodeMirror.Vim.defineAction('backslash', (cm) => {
    cm.replaceSelection('\\')
});
CodeMirror.Vim.defineAction('caret', (cm) => {
    cm.replaceSelection('^')
});
CodeMirror.Vim.defineAction('six', (cm) => {
    cm.replaceSelection('6')
});
CodeMirror.Vim.defineAction('myNewline', (cm) => {
    cm.replaceSelection('\n')
});

CodeMirror.Vim.mapCommand('//', 'action', 'backslash', {}, {
    context: 'insert'
});
CodeMirror.Vim.mapCommand('vv', 'action', 'caret', {}, {
    context: 'insert'
});
CodeMirror.Vim.mapCommand('99', 'action', 'six', {}, {
    context: 'insert'
});
CodeMirror.Vim.mapCommand('jj', 'action', 'myNewline', {}, {
    context: 'insert'
});
CodeMirror.Vim.mapCommand('mm', 'action', 'myNewline', {}, {
    context: 'insert'
});