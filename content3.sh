#!/bin/bash
 
cp /sys/class/power_supply/BAT0/uevent /opt/mybatop/uevent

cd /opt/mybatop

tr -s '[:blank:]' '-' < uevent > uevent1

date "+%D %T" > datefile

while read l;do echo $l | sed "s/POWER_SUPPLY_//";done < uevent1  > total.txt

while read n; do echo $n | sed "s/.*=//";done < total.txt > y.txt

u=()
while read w;do u+=("$w");done < datefile
u+=("Active")
while read p;do u+=("$p");done < y.txt

echo ${u[@]} > y1.txt

tr -s '[:blank:]' ',' < y1.txt > maindata.n

rm -rf uevent uevent1 datefile x.txt y.txt x1.txt y1.txt total.txt

