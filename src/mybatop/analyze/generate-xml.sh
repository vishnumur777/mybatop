#!/bin/bash

cd /opt/mybatop/analyze/pythonscripts || exit

cp /opt/mybatop/data/final.csv data.csv

python3 clean_dataset.py

{
  echo '<?xml version="1.0" encoding="UTF-8"?>'
  echo '<report>'
} >battery_report.xml

process_xml_section() {
  local tag=$1
  local script=$2
  local filename=$3

  echo "<${tag}>" >>battery_report.xml
  python3 "${script}" --xml
  tail -n +2 "${filename}" >>battery_report.xml
  echo "</${tag}>" >>battery_report.xml
}

mkdir .temp_xml_files

# Process all sections
process_xml_section "recent-usage" analyzers.py ".temp_xml_files/recent_usage.xml"
process_xml_section "technical-specification" tech_spec.py ".temp_xml_files/tech_spec.xml"
process_xml_section "average-capacity" dchar.py ".temp_xml_files/Average_capacity.xml"
process_xml_section "battery-capacity-history" batcaphis.py ".temp_xml_files/batcaphis.xml"
process_xml_section "battery-health" battery_health.py ".temp_xml_files/battery-health.xml"
process_xml_section "cycle-count" cycle_counts.py ".temp_xml_files/cycle_count.xml"
process_xml_section "battery-usage-activity" battery_activity.py ".temp_xml_files/battery_activity.xml"

# Close root element
echo "</report>" >>battery_report.xml

rm -rf .temp_xml_files data.csv

