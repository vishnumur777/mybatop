#!/bin/bash

cd /opt/mybatop/ || exit

./scripts/header.sh

cat headerfile temporaryfiler.n > final.csv

rm -rf headerfile
