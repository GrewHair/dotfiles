#!/bin/bash
#echo "jseval -q -f edit-tiddler-enumerate_elements.js" >> "$QUTE_FIFO"
echo "jseval -q elements=document.querySelectorAll('.tc-image-edit-button,.tc-edit-texteditor,.CodeMirror-lines');l=elements.length;for(let index=0;index<l;index++){elements[index].setAttribute('id', index + 10)}" >> "$QUTE_FIFO"
echo "hint edit-tiddler userscript edit-tiddler-hint.py" >> "$QUTE_FIFO"
