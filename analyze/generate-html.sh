#!/bin/bash

function addDiv(){
    echo "<div><h3 class=""title>$2</h3>""</div><p>$3</p>" > ad.txt
    cat ad.txt $1 > res
    rm -rf $1 ad.txt
    mv res $1
}

bash /opt/mybatop/main.sh

cp /opt/mybatop/final.csv /opt/mybatop/analyze/data.csv

cd /opt/mybatop/analyze

bash fetchuserdetails.sh

rm -rf merge.html

python3 combine.py

addDiv a.html "Recent Usage" "For last 3 days."

addDiv b.html "Technical Specification" "For last 3 days."

addDiv c.html  "Average capacity" "For 1 month."

addDiv d.html "Battery Capacity History" "Since the installation of lsbatt."

addDiv e.html "Battery Usage Activity" "Since the installation of lsbatt."

echo "</div>" > y2

cat *.html > temp.html

cat temp.html y2 > temp1.html

cat head.txt temp1.html tail.txt > merge.html

# cp merge.html .

rm -rf temp.html details.csv temp1.html y2 recent_3_days.csv a0.html a.html b.html c.html d.html e.html