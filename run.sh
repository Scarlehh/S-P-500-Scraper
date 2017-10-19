#!/bin/bash

source venv/bin/activate
echo "Running scraper..."
python3 scraper.py > stocksplit
echo "Scraper finished"
echo "Formatting data..."
sum=$(awk -F ' ' '{SUM = SUM + $2} END {print SUM}' stocksplit)
awk -F ' ' "{b=\$1"'"'":\t"'"'"(((\$2 / $sum)*50000)/\$3); print b}" stocksplit
echo "Finished! Enjoy :)"
