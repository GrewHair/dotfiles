#!/bin/bash
kill -9 $(ps -ef | grep 'steam' | grep -v grep | grep -v 'kill_all' |  awk '{print $2}')
kill -9 $(ps -ef | grep 'wine' | grep -v grep | grep -v 'kill_all' |  awk '{print $2}')
kill -9 $(ps -ef | grep 'retroarch' | grep -v grep | grep -v 'kill_all' |  awk '{print $2}')
kill -9 $(ps -ef | grep 'qjoypad' | grep -v grep | grep -v 'kill_all' |  awk '{print $2}')
