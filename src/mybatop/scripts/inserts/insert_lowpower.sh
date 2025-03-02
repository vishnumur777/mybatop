#!/bin/bash

cd /opt/mybatop/src/scripts/contents/;
./content_lowpower.sh
cat *.n > temporaryfiler.n
rm -rf maindata.n
