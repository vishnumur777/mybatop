#!/bin/bash

function addDiv() {
  echo "<div><h3 class=""title>$2</h3>""</div><p>$3</p>" >ad.txt
  cat ad.txt "$1" >res
  rm -rf "$1" ad.txt
  mv res "$1"
}

bash /opt/mybatop/generate-csv.sh

cp /opt/mybatop/data/final.csv /opt/mybatop/analyze/pythonscripts/data.csv

cd /opt/mybatop/analyze || exit

bash fetchuserdetails.sh

rm -rf merge.html

bash generate_classes.sh

cycle_count=$(cat /sys/class/power_supply/BAT0/cycle_count)

if [[ $cycle_count != 0 ]]; then
  python3 cycle_counts.py --graph
  addDiv f.html "Battery Cycle Count over Time" "Since the installation of mybatop."
else
  echo "Battery Cycle Count is not available in your device."
fi

addDiv a.html "Recent Usage" "For last 3 days."

addDiv b.html "Technical Specification" "For last 3 days."

addDiv c.html "Average capacity" "For 1 month."

addDiv d.html "Battery Capacity History" "Since the installation of mybatop."

addDiv e.html "Battery Health over Time" "Since the installation of mybatop."

if [[ -f "g.html" ]]; then
  addDiv g.html "Battery Usage Activity" "Since the installation of mybatop."
else
  echo "Battery Usage Activity will be enabled after few days."
fi
echo "</div>" >y2

cat ./*.html >temp.html

cat temp.html y2 >temp1.html

cat head.txt temp1.html tail.txt >merge.html

rm -rf temp.html data.csv details.csv temp1.html y2 recent_3_days.csv a0.html a.html b.html c.html d.html e.html f.html g.html
