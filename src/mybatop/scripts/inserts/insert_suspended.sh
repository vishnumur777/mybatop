#!/bin/bash

cd /opt/mybatop/src/scripts/contents/
./content_suspended.sh
cat *.n > temporaryfiler.n
rm -rf maindata2.n
