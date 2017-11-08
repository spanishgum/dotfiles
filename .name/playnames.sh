while true; do
for f in *; do
    if [[ $f == *'.art' ]] && [ ! -d $f ]; then
        if [ `wc -L $f | awk '{print $1}'` -lt `tput cols` ]; then
            clear
            echo $f
            cat $f
            sleep 1
        fi
    fi
done
done