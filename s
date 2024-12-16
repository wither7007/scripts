#!/bin/bash
if [ $# -eq 0 ]
  then
    # echo "No arguments supplied"
    days=2
    fd -H -I --changed-within="$days"days --ignore-file ~/.fdignore
  else 
    days=$1
  fd -H -I --changed-within="$days"days --ignore-file ~/.fdignore
    # echo "$1"
fi

