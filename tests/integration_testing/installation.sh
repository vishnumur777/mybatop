#!/bin/bash

cp src/mybatop/* /opt/mybatop/

mkdir /opt/mybatop/data

chmod -R 777 /opt/mybatop

chown -R $USER:$USER /opt/mybatop

ln -s /opt/mybatop/scripts/runscript/mybatop /usr/local/bin/mybatop