#!/bin/bash

# create folder for scraped web pages
mkdir archive

# set cron job
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
(crontab -l; echo "*/15 * * * * python $SCRIPTPATH/web-scraper.py")|awk '!x[$0]++'|crontab -
# * * * * * echo "CronTest: $(date)" >> /tmp/hello

# todo: make web-scraper.py runable (not working)
# sudo chmod +x web-scraper.py
