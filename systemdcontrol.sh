#!/bin/bash

echo "what do you wanna work with systemd service"
echo "1. start mybatop-start.service"
echo "2. stop mybatop-start.service"
echo "3. start mybatop-shutdown.service"
echo "4. stop mybatop-shutdown.service"

read y

if [[ $y -eq 1 ]]
then
	sudo systemctl disable mybatop-start.service
	sudo systemctl enable mybatop-start.service
	sudo systemctl start mybatop-start.service

elif [[ $y -eq 2 ]]
then
	sudo systemctl disable mybatop-start.service
	sudo systemctl stop mybatop-start.service

elif [[ $y -eq 3 ]]
then
	sudo systemctl disable mybatop-shutdown.service
	sudo systemctl enable mybatop-shutdown.service
	sudo systemctl start mybatop-shutdown.service

elif [[ $y -eq 4 ]]
then
	sudo systemctl disable mybatop-shutdown.service
	sudo systemctl stop mybatop-shutdown.service
else
	echo "Invalid option"
fi
