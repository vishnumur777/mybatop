#!/bin/bash

cd /opt/mybatop/src/scripts/contents/
./content_suspended.sh
cat *.n > tempo.n
cp tempo.n temporaryfiler.n
rm -rf tempo.n maindata2.n
