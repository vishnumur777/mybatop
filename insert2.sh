#!/bin/bash

cd /opt/mybatop
./content2.sh
cat *.n > tempo.n
cp tempo.n temporaryfiler.n
rm -rf tempo.n maindata2.n
