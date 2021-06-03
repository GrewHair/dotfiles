#!/bin/bash
#[ -p ~/kaldi-pipe ] || mkfifo ~/kaldi-pipe
#ps aux | grep kaldi_module_loader_plus | grep -v grep && exit 0
kill -9 $(ps aux | grep -G "python -u.*kaldi_module_loader_plus" | grep -v grep)
cd ~/kaldi-grammar-simple
~/env/bin/python -u kaldi_module_loader_plus.py > /tmp/kaldi-file #&
#echo $! > /tmp/kaldi-pid
#fg
#echo "Kaldi OFF" > /tmp/kaldi-file
exit 0
