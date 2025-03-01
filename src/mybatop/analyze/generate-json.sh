#!/bin/bash

cd pythonscripts

touch battery_report.json

echo "[" > battery_report.json

python3 analyzers.py --json

echo '{"Recent Usage":' >> battery_report.json

cat index.json >> battery_report.json

echo "}," >> battery_report.json

python3 tech_spec.py --json

echo '{"Technical Specification":' >> battery_report.json

cat index.json >> battery_report.json

echo "}," >> battery_report.json

python3 dchar.py --json

echo '{"Average Capacity":' >> battery_report.json

cat index.json >> battery_report.json

echo "}," >> battery_report.json

python3 batcaphis.py --json

echo '{"Battery Capacity History":' >> battery_report.json

cat index.json >> battery_report.json

echo "}," >> battery_report.json

python3 battery_activity.py --json

echo '{"Battery Usage":' >> battery_report.json

cat index.json >> battery_report.json

echo "}" >> battery_report.json

echo "]" >> battery_report.json

rm -rf index.json