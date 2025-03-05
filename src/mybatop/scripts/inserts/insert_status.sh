#!/bin/bash

read -r prev_status < /sys/class/power_supply/BAT0/status

extract_state() {
  cat /proc/acpi/button/lid/LID0/state | tr -s ' ' ',' | cut -d ',' -f 2
}

insert_status() {
    if [ "$state_read" != "Not charging" ] && [ "$state_read" != "Not-charging" ] && [ "$state_read" != "Unknown" ] && [ "$battery_state" == "closed" ]
    then
	/opt/mybatop/scripts/inserts/insert_active.sh
    fi
}

while true; do
   battery_status=$(extract_state)
   read -r state_read < /sys/class/power_supply/BAT0/status
   if [[ "$state_read" != "$prev_status" ]]; then
       	insert_status
       	prev_status="$state_read"
   fi

   sleep 10
done
