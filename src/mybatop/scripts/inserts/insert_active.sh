#!/bin/bash

cd /opt/mybatop/ || exit
./opt/mybatop/scripts/contents/content_active.sh
cat ./*.n > /opt/mybatop/data/tempo.n
cp /opt/mybatop/data/tempo.n /opt/mybatop/data/temporaryfiler.n
rm -rf /opt/mybatop/data/maindata.n
