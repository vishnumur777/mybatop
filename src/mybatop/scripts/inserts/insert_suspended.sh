#!/bin/bash

cd /opt/mybatop/src/scripts/contents/ || exit
./opt/mybatop/scripts/contents/content_suspended.sh
cat ./*.n > temporaryfiler.n
rm -rf maindata2.n
