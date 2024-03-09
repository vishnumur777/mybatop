#!/bin/bash

cd /opt/mybatop

./header.sh

cat headerfile temporaryfiler.n > final.csv

rm -rf headerfile
