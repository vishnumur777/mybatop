#!/bin/bash
 
cd /opt/mybatop || exit

tr -s '[:blank:]' '-' < /sys/class/power_supply/BAT0/uevent | sed -e 's/POWER_SUPPLY_//' -e 's/.*=//' > y.txt

datevalue=$(date "+%D %T")

mapfile -t content < y.txt

u=("$datevalue" "Low Power" "${content[@]}")

echo "${u[@]}" | tr -s '[:blank:]' ',' > /opt/mybatop/data/maindata.n

rm -rf y.txt datefile
