p=/home/$USER
f=.name

if [ ! -d $p/$f ]; then
    if [ ! -d $p/dotfiles/$f ]; then
        echo 'No name art found, exiting...'
    else
        cat $p/dotfiles/$f/art.txt
    fi
else
    cat $p/$f/art.txt
fi
echo ""