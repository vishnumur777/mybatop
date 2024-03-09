#!/bin/bash

cd /opt/mybatop

cp /sys/class/power_supply/BAT0/uevent /opt/mybatop/uevent

while read l;do echo $l | sed "s/POWER_SUPPLY_//";done < /opt/mybatop/uevent > /opt/mybatop/total.txt

while read m; do echo $m | sed "s/=.*//";done < /opt/mybatop/total.txt > /opt/mybatop/x.txt

t+=( "DATE" "TIME" "STATUS" )

while read o;do t+=("$o");done < /opt/mybatop/x.txt

t[5]="SOURCE"

echo ${t[@]} > /opt/mybatop/x1.txt

tr -s '[:blank:]' ',' < /opt/mybatop/x1.txt > /opt/mybatop/headerfile

rm -rf uevent total.txt x.txt x1.txt
