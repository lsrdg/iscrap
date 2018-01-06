#!/bin/bash


if [ $# -eq 0 ]
then
    python ~/git/iscrap/iscrap.py fetch 3; sudo pacman -Syu;

elif [ $1 == 'read' ]; then
    python ~/git/iscrap/iscrap.py read $2;
fi

#http://ryanstutorials.net/bash-scripting-tutorial/bash-variables.php1
