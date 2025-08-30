#!/bin/bash

mkdir -p /opt/mybatop/data

cp src/mybatop/* /opt/mybatop/

chmod -R 777 /opt/mybatop

chown -R $USER:$USER /opt/mybatop

ln -s /opt/mybatop/scripts/runscript/mybatop /usr/local/bin/mybatop