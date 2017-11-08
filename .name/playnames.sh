IFS=$'\n'
while true; do
for f in `find favs -maxdepth 1 -iname '*.art' -type f | shuf`; do
    fcol=`wc -L $f | awk '{print $1}'`
    frow=`wc -l $f | awk '{print $1}'`
    col=`tput cols`
    row=`tput lines`
    if [ $fcol -lt $col ] && [ $frow -lt $row ]; then
        let xcol=($col-$fcol)/2 && let xrow=($row-$frow)/2
        yes '' | sed ${xrow}q # vertical center first, then horizontal
        for i in $(cat $f); do printf "%*s$i" $xcol | tr ' ' " "; echo ""; done
        sleep 1
        clear
    fi
done
done
