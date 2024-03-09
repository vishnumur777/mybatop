#!/bin/bash

cd /opt/mybatop;
./content.sh
cat *.n > tempo.n
cp tempo.n temporaryfiler.n
rm -rf tempo.n maindata.n
