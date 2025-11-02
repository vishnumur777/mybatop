#!/bin/bash

host_name=$(hostname -f)
sys_name=$(sudo dmidecode -s system-product-name)
os_name=$(cat /etc/os-release | awk -F '=' 'NR==1 {print $2}' | sed -e 's/"//g')
report_time=$(date +%D)" "$(date +%T)
dates=$(date +%D)
times=$(date +%T)

echo '<div class="report-header">' >webheader.txt
echo '<h1 style="font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Roboto Mono, Courier New, monospace; font-weight: Bold;font-size: 50px; color: #FFFFFF;margin-left: 55px">Battery Diagnostic Report</h1>' >>webheader.txt
echo "<p style='margin-left: 55px'> $sys_name | $os_name </p>" >>webheader.txt
echo '<div class="report-meta">' >>webheader.txt
echo "Battery Report — <span style="color:#e6eef3"> $host_name </span> @ $times, $dates " >>webheader.txt
echo '</div></div>' >>webheader.txt
