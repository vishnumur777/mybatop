#!/bin/bash

sudo mkdir /opt/mybatop

sudo cp -r * /opt/mybatop

sudo cp -r filesystemd/* /etc/systemd/system

cd /opt/mybatop

sudo touch temporaryfiler.n

sudo chmod -R +rwx *

sudo chown -R $USER:$USER /opt/mybatop/

echo 'export PATH="$PATH:/opt/mybatop"' >>~/.bashrc

echo 'alias mybatop=/opt/mybatop/mainscript/mybatop' >> ~/.bashrc

sudo systemctl daemon-reload

sudo systemctl enable mybatop-shutdown.service

sudo systemctl enable mybatop-startup.service

sudo systemctl enable mybatop-status.service

sudo systemctl start mybatop-startup.service

sudo systemctl start mybatop-status.service

sudo systemctl start mybatop-shutdown.service

sudo pip install pandas --break-system-packages

sudo pip install plotly-express --break-system-packages

source ~/.bashrc

