#!/bin/bash

cd /opt/mybatop/;
./opt/mybatop/scripts/contents/content_lowpower.sh
cat *.n > tempo.n
cp tempo.n temporaryfiler.n
rm -rf tempo.n maindata.n
