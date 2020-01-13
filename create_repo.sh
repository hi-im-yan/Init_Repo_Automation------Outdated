#!/bin/bash
function creating() {
    python new_repo.py $1
    cd C:/Users/yanaj/Projetos/$1
    echo "Connecting folder to repository..."
    echo 
    git init
    git remote add origin https://github.com/hi-im-yan/$1.git
    touch README.md
    git add .
    git commit -m "First commit"
    git push -u origin master
    git checkout -b developing
    code .
    echo
    echo "Enjoy your project :D"
}
creating $1