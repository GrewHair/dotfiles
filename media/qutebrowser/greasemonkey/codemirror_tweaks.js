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


CodeMirror.Vim.defineAction('vertical', (cm) => {
    cm.replaceSelection('│')
});
CodeMirror.Vim.defineAction('verticalAndRight', (cm) => {
    cm.replaceSelection('├')
});
CodeMirror.Vim.defineAction('horizontal', (cm) => {
    cm.replaceSelection('─')
});
CodeMirror.Vim.defineAction('upAndRight', (cm) => {
    cm.replaceSelection('└')
});
CodeMirror.Vim.defineAction('downAndHorizontal', (cm) => {
    cm.replaceSelection('┬')
});




CodeMirror.Vim.mapCommand('j/', 'action', 'backslash', {}, {
    context: 'insert'
});
CodeMirror.Vim.mapCommand('jv', 'action', 'caret', {}, {
    context: 'insert'
});
CodeMirror.Vim.mapCommand('j9', 'action', 'six', {}, {
    context: 'insert'
});
CodeMirror.Vim.mapCommand('f/', 'action', 'backslash', {}, {
  context: 'insert'
});
CodeMirror.Vim.mapCommand('fv', 'action', 'caret', {}, {
  context: 'insert'
});
CodeMirror.Vim.mapCommand('f9', 'action', 'six', {}, {
  context: 'insert'
});


CodeMirror.Vim.mapCommand('ji', 'action', 'vertical', {}, {
    context: 'insert'
});
CodeMirror.Vim.mapCommand('je', 'action', 'verticalAndRight', {}, {
    context: 'insert'
});
CodeMirror.Vim.mapCommand('j-', 'action', 'horizontal', {}, {
    context: 'insert'
});
CodeMirror.Vim.mapCommand('jl', 'action', 'upAndRight', {}, {
    context: 'insert'
});
CodeMirror.Vim.mapCommand('jt', 'action', 'downAndHorizontal', {}, {
    context: 'insert'
});
CodeMirror.Vim.mapCommand('fi', 'action', 'vertical', {}, {
  context: 'insert'
});
CodeMirror.Vim.mapCommand('fe', 'action', 'verticalAndRight', {}, {
  context: 'insert'
});
CodeMirror.Vim.mapCommand('f-', 'action', 'horizontal', {}, {
  context: 'insert'
});
CodeMirror.Vim.mapCommand('fl', 'action', 'upAndRight', {}, {
  context: 'insert'
});
CodeMirror.Vim.mapCommand('ft', 'action', 'downAndHorizontal', {}, {
  context: 'insert'
});
