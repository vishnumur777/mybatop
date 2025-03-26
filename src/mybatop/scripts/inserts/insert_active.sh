#!/bin/bash

cd /opt/mybatop/ || exit
./opt/mybatop/scripts/contents/content_active.sh
cat ./*.n > temporaryfiler.n
rm -rf maindata.n
