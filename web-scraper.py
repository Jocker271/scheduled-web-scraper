import csv
from datetime import datetime
import urllib.request


def get_url_list():
    """
    Reads the url_list.csv and returns all urls
    @return: list[str] -> list of urls
    """
    with open("./url_list.csv", 'r') as url_file:
        csvreader = csv.reader(url_file)
        next(csvreader)
        url_list = [row[0] for row in csvreader if row]
    return url_list


def fetch_web_pages():
    """Requests all urls
    Prints Error Messages for failing requests.
    """
    url_list = (get_url_list())
    for url in url_list:
        try:
            web_page = urllib.request.urlopen(url)
            result_code = web_page.getcode()
            if result_code != 200:
                print(f"Code {result_code} for: {url}")
                continue
            save_page_to_file(web_page)
        except ValueError:
            print(f"Failed request for: {url}")


def save_page_to_file(web_page):
    page_content = web_page.read()
    if page_content:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        url_name = web_page.url.split("//")[1].replace(
            ".", "_").replace("/", "_")
        file_name = f"{url_name}_{timestamp}"
        with open(f"./archive/{file_name}.html", "wb") as new_file:
            new_file.write(page_content)


def print_all_cookies(web_page):
    # print all the cookies
    cookies = list(
        filter(lambda x: x[0] == "Set-Cookie", web_page.headers.items()))
    for crumb in cookies:
        cookie_name, cookie_value = crumb[1].split("=", 1)
        print(cookie_name, cookie_value.split(";")[0])


if __name__ == '__main__':
    fetch_web_pages()
