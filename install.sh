#!/bin/bash

sudo mkdir /opt/mybatop

sudo cp -r * /opt/mybatop

sudo cp -r filesystemd/* /etc/systemd/system

cd /opt/mybatop

sudo touch temporaryfiler.n

sudo chmod -R +rwx *

sudo chown -R $USER:$USER /opt/mybatop/

echo 'export PATH="$PATH:/opt/mybatop:/opt/mybatop/mainscript/"' >>~/.bashrc

# echo 'alias mybatop="sudo /opt/mybatop/mainscript/mybatop"' >> ~/.bashrc

sudo systemctl daemon-reload

sudo systemctl enable --now mybatop-shutdown.service

sudo systemctl enable --now mybatop-startup.service

sudo systemctl enable --now mybatop-status.service

sudo pip install pandas --break-system-packages

sudo pip install plotly-express --break-system-packages

source ~/.bashrc

