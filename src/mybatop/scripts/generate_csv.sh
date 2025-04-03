#!/bin/bash

cd /opt/mybatop/ || exit

./scripts/header.sh

cd data/ || exit

cat headerfile temporaryfiler.n > final.csv

rm -rf headerfile
