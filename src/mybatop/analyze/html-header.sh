#!/bin/bash

host_name=$(hostname -f)
sys_name=$(sudo dmidecode -s system-product-name)
os_name=$(awk -F '=' 'NR==1 {gsub(/"/,"",$2);print $2}' /etc/os-release)
dates=$(date +%D)
times=$(date +%T)

{
  echo '<div class="report-header">'
  echo '<h1 style="font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Roboto Mono, Courier New, monospace; font-weight: Bold;font-size: 50px; color: #FFFFFF;margin-left: 55px">Battery Diagnostic Report</h1>'
  echo "<p style='margin-left: 55px'> $sys_name | $os_name </p>"
  echo '<div class="report-meta">'
  echo "Battery Report — <span style=\"color:#e6eef3\"> $host_name </span> @ $times, $dates "
  echo '</div></div>'
} >webheader.txt
