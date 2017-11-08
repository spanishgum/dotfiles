while true; do
for f in `find art -maxdepth 1 -iname '*.art' -type f | shuf`; do
    if [ `wc -L $f | awk '{print $1}'` -lt `tput cols` ]; then
        clear && cat $f && sleep 1
    fi
done
done
