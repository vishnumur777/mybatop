#!/bin/bash

extract_state() {
  cat /proc/acpi/button/lid/LID0/state | tr -s ' ' ',' | cut -d ',' -f 2
}

prev_state=$(extract_state)

while true; do
  if [[ "$current_state" != "$prev_state" ]]; then
    if [[ "$current_state" == "closed" ]]; then
      /opt/mybatop/insert_lowpower.sh
    elif [[ "$current_state" == "open" ]]; then
      /opt/mybatop/insert.sh
    fi
    prev_state="$current_state"
  fi
  sleep 3
done
