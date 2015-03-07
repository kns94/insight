#!/bin/sh
cd wc_input && find . -iname '*~' -delete
cd ..
python Word_Count.py
python Median.py


