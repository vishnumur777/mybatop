#!/bin/bash

cd /opt/mybatop || exit

sed -e "s/POWER_SUPPLY_//" -e "s/=.*//" < /sys/class/power_supply/BAT0/uevent > /opt/mybatop/data/x.txt

mapfile -t header < /opt/mybatop/data/x.txt

t=()
t+=("DATE" "TIME" "STATE" "${header[@]}")
t[5]="SOURCE"

echo "${t[@]}" | tr -s '[:blank:]' ',' > /opt/mybatop/data/headerfile

rm -rf /opt/mybatop/data/x.txt
