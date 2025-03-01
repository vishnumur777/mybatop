#!/bin/bash

cd pythonscripts

touch battery_report.xml

echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" >> battery_report.xml 

echo "<report>" >> battery_report.xml

echo "<recent-usage>" >> battery_report.xml

python3 analyzers.py --xml

cat index.xml | tail -n +2 >> battery_report.xml

echo "</recent-usage>" >> battery_report.xml

echo "<technical-specification>" >> battery_report.xml

python3 tech_spec.py --xml

cat index.xml | tail -n +2 >> battery_report.xml

echo "</technical-specification>" >> battery_report.xml

echo "<average-capacity>" >> battery_report.xml

python3 dchar.py --xml

cat index.xml | tail -n +2 >> battery_report.xml

echo "</average-capacity>" >> battery_report.xml

echo "<battery-capacity-history>" >> battery_report.xml

python3 batcaphis.py --xml

cat index.xml | tail -n +2 >> battery_report.xml

echo "</battery-capacity-history>" >> battery_report.xml

echo "<battery-usage-activity>" >> battery_report.xml

python3 battery_activity.py --xml

cat index.xml | tail -n +2 >> battery_report.xml

echo "</battery-usage-activity>" >> battery_report.xml

echo "</report>" >> battery_report.xml

# rm -rf index.xml