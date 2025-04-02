#!/bin/bash

cd pythonscripts || exit

cp /opt/mybatop/data/final.csv /opt/mybatop/analyze/data.csv

{
    echo "["
} > battery_report.json

add_comma() {
    echo "," >> battery_report.json
}

process_section() {
    python3 "$1" --json
    {
        echo "{\"$2\":"
        cat "$3"
        echo "}"
    } >> battery_report.json
}

process_section analyzers.py "Recent Usage" "recent_usage.json" && add_comma
process_section tech_spec.py "Technical Specification" "tech_spec.json" && add_comma
process_section dchar.py "Average Capacity" "average_capacity.json" && add_comma
process_section battery_health.py "Battery Health" "battery_health.json" && add_comma
process_section cycle_counts.py "Cycle Counts" "cycle_counts.json" && add_comma
process_section batcaphis.py "Battery Capacity History" "batcaphis.json" && add_comma
process_section battery_activity.py "Battery Usage" "battery_activity.json"

{
    echo "]"
} >> battery_report.json


rm -rf data.csv recent_usage.json tech_spec.json average_capacity.json battery_health.json cycle_counts.json batcaphis.json battery_activity.json