#!/bin/bash

cd pythonscripts/

python3 analyzers.py --html

python3 tech_spec.py --html

python3 batcaphis.py --html

python3 battery_activity.py --html

python3 dchar.py --graph

python3 userdetails.py

mv *.html ..

