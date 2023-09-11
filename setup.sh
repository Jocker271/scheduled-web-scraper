#!/bin/bash

# create folder for scraped web pages
mkdir archive

# set cron job that runs web.scraper.py every 15 minutes
SCRIPTPATH="$( cd -- "$(dirname "$0")" || exit >/dev/null 2>&1 ; pwd -P )"
(crontab -l; echo "*/1 * * * * python $SCRIPTPATH/web-scraper.py")|awk '!x[$0]++'|crontab -

# start cron jobs
service cron start
