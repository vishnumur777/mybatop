#!/bin/bash

cd /opt/mybatop/

./scripts/header.sh

cat headerfile temporaryfiler.n > final.csv

rm -rf headerfile