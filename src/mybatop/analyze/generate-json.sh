#!/bin/bash

cd /opt/mybatop/analyze/pythonscripts || exit

cp /opt/mybatop/data/final.csv data.csv

{
  echo "["
} >battery_report.json

add_comma() {
  echo "," >>battery_report.json
}

process_section() {
  python3 "$1" --json
  {
    echo "{\"$2\":"
    cat "$3"
    echo "}"
  } >>battery_report.json
}

mkdir .temp_json_files/

process_section analyzers.py "Recent Usage" ".temp_json_files/recent_usage.json" && add_comma
process_section tech_spec.py "Technical Specification" ".temp_json_files/tech_spec.json" && add_comma
process_section dchar.py "Average Capacity" ".temp_json_files/average_capacity.json" && add_comma
process_section battery_health.py "Battery Health" ".temp_json_files/battery_health.json" && add_comma
process_section cycle_counts.py "Cycle Counts" ".temp_json_files/cycle_counts.json" && add_comma
process_section batcaphis.py "Battery Capacity History" ".temp_json_files/batcaphis.json" && add_comma
process_section battery_activity.py "Battery Usage" ".temp_json_files/battery_activity.json"

{
  echo "]"
} >>battery_report.json

rm -rf data.csv recent_usage.json tech_spec.json average_capacity.json battery_health.json cycle_counts.json batcaphis.json battery_activity.json

