#!/bin/bash
kill -9 $(ps -ef | grep 'qjoypad' | grep -v grep | grep -v stop |  awk '{print $2}')
