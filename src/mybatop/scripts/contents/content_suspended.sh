#!/bin/bash
 
cd /opt/mybatop

tr -s '[:blank:]' '-' < /sys/class/power_supply/BAT0/uevent | sed -e 's/POWER_SUPPLY_//' -e 's/.*=//' > y.txt

datevalue=$(date "+%D %T")

mapfile -t content < y.txt

u=("$datevalue" "Suspended" "${content[@]}")

echo "${u[@]}" | tr -s '[:blank:]' ',' > maindata2.n

rm -rf y.txt datefile