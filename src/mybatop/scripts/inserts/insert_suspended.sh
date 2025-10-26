#!/bin/bash

cd /opt/mybatop/data/ || exit
bash /opt/mybatop/scripts/contents/content_suspended.sh
cat ./*.n >  tempo.n
cp  tempo.n  temporaryfiler.n
rm -rf maindata2.n tempo.n
