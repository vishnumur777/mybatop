#!/bin/bash

extract_state() {
  tr -s ' ' ',' < /proc/acpi/button/lid/LID0/state | cut -d ',' -f 2
}

insert_status() {
    stat=$(cat /sys/class/power_supply/BAT0/status)
    if [ "$stat" != "Not charging" ] && [ "$stat" != "Not-charging" ] && [ "$stat" != "Unknown" ]
    then
	    echo "$stat"
    fi
}

prev_state=$(extract_state)
prev_status=$(insert_status)

while true; do
  current_state=$(extract_state)
  current_status=$(insert_status)
  if [[ "$current_state" != "$prev_state" ]]; then
    if [[ "$current_state" == "closed" ]]; then
      /opt/mybatop/insert_lowpower.sh
    elif [[ "$current_state" == "open" ]]; then
      /opt/mybatop/insert.sh
    fi
    prev_state="$current_state"
  fi

  if [ "$current_status" != "$prev_status" ]; then
    if [ "$current_state" = "closed" ]; then
      /opt/mybatop/insert_lowpower.sh
    fi
    prev_status="$current_status"
  fi

  sleep 3
done
