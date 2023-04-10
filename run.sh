#!/bin/bash

LINK=${1?Error: no playlist url given}
wget -q -O - $LINK | grep -oP '(, )?<a href="/artist/.*?">.*?</a>|<a .*? href="/track/.*?">.+?</a>' > src.html
python3 scraper.py
