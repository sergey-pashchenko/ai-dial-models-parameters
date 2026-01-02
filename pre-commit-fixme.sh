#!/bin/sh
# https://gist.github.com/kuy/5d1151fd5897a9b84c06

matches=$(git diff --staged | grep -E '\+.*?FIXME')

if [ "$matches" != "" ]
then
    echo "'FIXME' tag is detected."
    echo "Please fix it before committing."
    echo "  ${matches}"
    exit 1
fi
