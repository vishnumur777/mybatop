#!/bin/bash

cd /opt/mybatop/src

./header.sh

cat headerfile temporaryfiler.n > final.csv

rm -rf headerfile