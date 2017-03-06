#!/bin/bash


if [ $# -eq 0 ]
then
    python ~/git/iscrap/iscrap.py --fetch ; sudo pacman -Syu;

elif [ $1 == '-r' ]; then
    python ~/git/iscrap/iscrap.py --read $2;
fi

#http://ryanstutorials.net/bash-scripting-tutorial/bash-variables.php1
