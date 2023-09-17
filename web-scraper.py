#!/usr/bin/python

import csv
import logging
import os
import urllib.request
from datetime import datetime
from logging.handlers import RotatingFileHandler

import config


def setup_logger():
    """Creates a logger and returns it"""
    filename = os.path.join(dir_path, "app.log")
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    max_bytes = config.logging_max_bytes * 1048576  # converts MiB to bytes
    handler = RotatingFileHandler(
        filename, maxBytes=max_bytes, backupCount=config.logging_backup_count)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s",
                                  config.logging_date_format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_url_list():
    """
    Reads the url_list.csv and returns all urls
    @return: list[str] -> list of urls
    """
    full_file_path = os.path.join(dir_path, "url_list.csv")
    with open(full_file_path, "r") as url_file:
        csvreader = csv.reader(url_file)
        next(csvreader)
        url_list = [row[0] for row in csvreader if row]
    return url_list


def save_page_to_file(web_page):
    """
    Writes the content of a web_page to a new created html file.
    @param web_page: request element
    """
    page_content = web_page.read()
    if page_content:
        timestamp = datetime.now().strftime(config.store_file_date_format)
        url_name = web_page.url.split("//")[1].replace(
            ".", "_").replace("/", "_")
        file_name = f"{url_name}_{timestamp}.html"
        full_file_path = os.path.join(dir_path, f"archive/{file_name}")
        with open(full_file_path, "wb") as new_file:
            new_file.write(page_content)


def fetch_web_pages():
    """
    Requests all urls.
    This is the main function to handle the webpage scraping
    """
    url_list = (get_url_list())
    page_counter = 0
    for url in url_list:
        try:
            web_page = urllib.request.urlopen(url)
            result_code = web_page.getcode()
            if result_code == 200:
                page_counter += 1
                if config.store_web_pages and available_memory:
                    save_page_to_file(web_page)
            else:
                logger.warning(f"Code {result_code} for '{url}'")
        except ValueError:
            logger.error(f"Failed request for '{url}'")
    if config.store_web_pages and not available_memory:
        logger.warning("Memory limit reached")
    logger.info(f"Scraped {page_counter} pages")


def get_available_memory():
    """
    Checks if there is enough memory according to the setting
    @return: boolean
    """
    archive_path = os.path.join(dir_path, "archive")
    dir_size = sum([os.path.getsize(x) for x in os.scandir(archive_path)])
    dir_size = dir_size / 1048576  # converts byte to MiB
    has_available_memory = config.max_storage_memory > dir_size
    return has_available_memory


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    logger = setup_logger()
    available_memory = get_available_memory()
    fetch_web_pages()
