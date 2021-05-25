#!/bin/sh

rm -r output/
python3 ./compile.py
cd output/
echo "Press ctrl-c to stop serving"
python3 -m http.server
