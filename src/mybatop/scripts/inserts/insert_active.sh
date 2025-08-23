#!/bin/bash

cd /opt/mybatop/data/ || exit
bash /opt/mybatop/scripts/contents/content_active.sh
cat ./*.n > tempo.n
cp tempo.n temporaryfiler.n
rm -rf maindata.n tempo.n