#!/bin/bash

read -r prev_status < /sys/class/power_supply/BAT0/status

insert_status() {
    if [ "$state_read" != "Not charging" ] && [ "$state_read" != "Not-charging" ] && [ "$state_read" != "Unknown" ]
    then
	    /opt/mybatop/scripts/inserts/insert_active.sh
    fi
}

while true; do
   read -r state_read < /sys/class/power_supply/BAT0/status
   if [[ "$state_read" != "$prev_status" ]]; then
       	insert_status
       	prev_status="$state_read"
   fi
   sleep 5
done
