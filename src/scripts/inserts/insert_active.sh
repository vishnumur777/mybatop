#!/bin/bash

cd /opt/mybatop/src/scripts/contents/;
./content_active.sh
cat *.n > tempo.n
cp tempo.n temporaryfiler.n
rm -rf tempo.n maindata.n
