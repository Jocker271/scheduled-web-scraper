#!/usr/bin/python

"""This file contains the settings of the web scraper script"""

# === General ===
random_delay_min = 0  # minutes
# random_delay_min hides the systematics of calls for the site operator.
# Should be coordinated with the time setting of the cron job. If the cron runs
# every 15 minutes, an optional delay of one hour is not useful.

# === Saving Web Pages ===
store_web_pages = True  # (True/False)
max_storage_memory = 12  # in MB
# TODO: path_to_storage_directory # allow absolute path to dir on other hardware
store_file_date_format = "%Y%m%d-%H%M"

# === Logging ===
logging_max_bytes = 1  # How many MB a log file can be (I advise a max. of 3)
logging_backup_count = 3  # How many log files will be stored
logging_date_format = "%Y-%m-%d %H:%M:%S"  # Dateformat of the log entries



