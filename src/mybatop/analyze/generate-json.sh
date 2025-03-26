#!/bin/bash

cd pythonscripts || exit

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
process_section batcaphis.py "Battery Capacity History" "batcaphis.json" && add_comma
process_section battery_activity.py "Battery Usage" "battery_activity.json"

{
    echo "]"
} >> battery_report.json


rm -rf index.json