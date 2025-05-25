#!/bin/bash

cd /opt/mybatop/src/scripts/contents/ || exit
./opt/mybatop/scripts/contents/content_suspended.sh
cat ./*.n > /opt/mybatop/data/tempo.n
cp /opt/mybatop/data/tempo.n /opt/mybatop/data/temporaryfiler.n
rm -rf maindata2.n
