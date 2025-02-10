#!/bin/bash

host_name=$(hostname -f)
sys_name=$(sudo dmidecode -s system-product-name)
bios_det=$(sudo dmidecode -s bios-vendor)" "$(sudo dmidecode -s bios-version)" "$(sudo dmidecode -s bios-release-date)
os_name=$(lsb_release -i | cut -f 2-)
report_time=$(date +%D)" "$(date +%T)

model_name=$(cat /sys/class/power_supply/BAT0/model_name)
bat_serial_no=$(cat /sys/class/power_supply/BAT0/serial_number)
type=$(cat /sys/class/power_supply/BAT0/type)
technology=$(cat /sys/class/power_supply/BAT0/technology)
manufacturer=$(cat /sys/class/power_supply/BAT0/manufacturer)
ch_full_d=$(( $(cat /sys/class/power_supply/BAT0/charge_full_design) / 1000 ))
volt_des=$(( $(cat /sys/class/power_supply/BAT0/voltage_min_design) / 1000 ))

echo "HOSTNAME,SYSTEM NAME,BIOS DETAILS,OS NAME,REPORT TIME,MODEL NAME,BATTERY SERIAL NUMBER,TYPE,TECHNOLOGY,MANUFACTURER,CHARGE FULL DESIGN,VOLTAGE MINIMUM DESIGN" >> details.csv
echo $host_name,$sys_name,$bios_det,$os_name,$report_time,$model_name,$bat_serial_no,$type,$technology,$manufacturer,$ch_full_d,$volt_des >> details.csv