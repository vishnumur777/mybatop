#!/bin/bash

cd pythonscripts || exit

cp /opt/mybatop/data/final.csv /opt/mybatop/analyze/data.csv

{
    echo '<?xml version="1.0" encoding="UTF-8"?>'
    echo '<report>'
} > battery_report.xml

process_xml_section() {
    local tag=$1
    local script=$2
    local filename=$3
    
    echo "<${tag}>" >> battery_report.xml
    python3 "${script}" --xml
    tail -n +2 "${filename}" >> battery_report.xml
    echo "</${tag}>" >> battery_report.xml
}

# Process all sections
process_xml_section "recent-usage" analyzers.py "recent_usage.xml"
process_xml_section "technical-specification" tech_spec.py "tech_spec.xml"
process_xml_section "average-capacity" dchar.py "Average_capacity.xml"
process_xml_section "battery-capacity-history" batcaphis.py "batcaphis.xml"
process_xml_section "battery-health" battery_health.py "battery-health.xml"
process_xml_section "cycle-count" cycle_counts.py "cycle_count.xml"
process_xml_section "battery-usage-activity" battery_activity.py "battery_activity.xml"

# Close root element
echo "</report>" >> battery_report.xml

# Move the generated XML file to the parent directory   
mv battery_report.xml ..
 
rm -rf ./*.xml