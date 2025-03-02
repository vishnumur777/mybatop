#!/bin/bash

extract_state(){
    cat /proc/acpi/button/lid/LID0/state | tr -s ' ' ',' | cut -d ',' -f 2
}

read -r prev_status < $(extract_state)

while true; do
   read -r state_read < $(extract_state)
   if [[ "$state_read" == "closed" ]]; then
       	/opt/mybatop/src/scripts/inserts/insert_lowpower.sh
       	prev_status="$state_read"
   elif [[ "$state_read" == "open" ]]; then
       	/opt/mybatop/src/scripts/inserts/insert_active.sh
       	prev_status="$state_read"
   fi
   sleep 3
done
