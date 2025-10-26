#!/bin/bash

cd /opt/mybatop/data || exit

sed -e "s/POWER_SUPPLY_//" -e "s/=.*//" < /sys/class/power_supply/BAT0/uevent >  x.txt

mapfile -t header <  x.txt

t=()
t+=("DATE" "TIME" "STATE" "${header[@]}")
t[5]="SOURCE"

echo "${t[@]}" | tr -s '[:blank:]' ',' >  headerfile

rm -rf  x.txt
