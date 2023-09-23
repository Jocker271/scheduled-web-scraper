# scheduled-web-scraper
This simple project is used to automatically generate backups of specific webpages.


[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
![Python](https://img.shields.io/badge/Python-v3.10-informational)
![Author](https://img.shields.io/badge/made_by-Jocker271-871c1c.svg?logo=data:image/svg%2bxml;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABG2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS41LjAiPgogPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIi8+CiA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgo8P3hwYWNrZXQgZW5kPSJyIj8+Gkqr6gAAAYNpQ0NQc1JHQiBJRUM2MTk2Ni0yLjEAACiRdZG7SwNBEIe/RIPigwixsLAI4qMxohFELSwSfIFaJCf4apLzLhGSeNxFRGwF24CCaOOr0L9AW8FaEBRFEAsra0UblXPOEyJiZpmdb3+7M+zOglfJqFmrvBOyubwZG44Ep6ZnghWP+PAToJ+2hGoZ4/EhhZL2doPHiVchp1bpc/9a9bxmqeCpFB5QDTMvPCI8tpw3HN4UrlfTiXnhY+F2Uy4ofO3oSZefHE65/OGwqcSi4K0TDqZ+cfIXq2kzKywvpzmbWVJ/7uO8pEbLTcYlNok3YhFjmAhBRhkkSg9d9MncQ4gwHbKiRH7nd/4Ei5KrymywgskCKdLkaRd1SaprEnXRNRkZVpz+/+2rpXeH3eo1EfA92PZLC1RswGfBtt/3bfvzAMru4SxXzF/cg95X0QtFrXkX/Gtwcl7Ukltwug4Nd0bCTHxLZeJeXYfnI6idhsAlVM26PfvZ5/AWlFX5qgvY3oFWOe+f+wK2OWgKPBfPJQAAAAlwSFlzAAALEwAACxMBAJqcGAAAAbhJREFUOI190ztok1EUB/DfbfM1jYOCDlLM4GB9QcHBgpNDHXSroIOLm0XwgYMg/aB7BEFRfCF0EJ2K1GZxqagUHEQUdXMQsVwptgqCj6SW5nNoKPFr4lkO9/B/cQ6XDlWfsqFWNVKr6oLFqm31KZfrVd2tuK5OAiFYFzIDITPUHPVnNHqHLbfiCjnX23hSXDZVz8yH4GAIBherioIxmUreqJB7TwiO1AuOhUw10MC+jFuBvhBsqpTLQ8jSGJ9CyCvWHtgcEo9DsHVpqVBcmCt+nZ/r6f78Mfkx+y6p176HfhxPY5xol0DpqC/PL2ycnH2fnJt9k3Q1lvWF4I/gZdbwATswvbqrvEClXB7AC5Qwgxt4lMb4s1IuP8T6NMYDnXYAvSiFbidGP8XxFuG9OIxTreB2Z3yFO9mymRZyCXex0OyrtSZBGmMDJ3PjS9iNsTTG3/8VaDom2IkBDOI0ariexxZyxC24gkO4h184gwyjzd5eoFIu9+AZ5rEH2zHZxKRpjNfapW1NsAubMIzzGEGCm2mMF9uRablCGuNbfMNrK6dKcB9nO5HzCWA/rlr5A+NpjNNrKf/WX7XEi5v348VCAAAAAElFTkSuQmCC)


## Installation
The Python script alone is not sufficient for a repetitive action, so we need to set up a cron job.
Of course, the cron job only runs when the computer is on, so the setup on a server is recommended.

### Automatically (Linux)
Run the `setup.sh`. You may have to make the file executable first with `chmod +x setup.sh`.

### Manually (Linux)
Since Git can't index empty folders and I don't want to work with a .gitkeep file, you need to manually create a folder called "archive" in this project with `mkdir archiv`.

Open the crontab file with `crontab -e` and create a new cron job by adding a line according to the given scheme (minute hour day month day-of-week command-line-to-execute).
The time parameters can be freely selected. However, the web scraper script must be called in the command. Make sure you specify the correct path to the python file. 

The new line could look like one of the following examples:
- Run the web-scraper every full hour:\
`0 * * * * /usr/stupid-web-scraper/main.py`
- Run the web-scraper every 15 minutes from 8 am to 6 pm from Monday to Friday:\
`*/15 8-18 * * 1-6 /usr/stupid-web-scraper/main.py`\
<sub>See [wiki.ubuntuusers.de/Cron](https://wiki.ubuntuusers.de/Cron/) for more information.</sub>

Save the file and make sure cron is actually running with `service cron status`.
If not you have to start the service with `sudo service cron start`.

## Usage
Store the links to all webpages to be called in `url_list.csv` file.
All other settings can be adjusted in `config.py` file.

Start the cron jobs
```bash
service cron start
```
\
Stop the cron jobs
```bash
service cron stop
```

___
## Roadmap

- [x] Core functionality to scrap multiple webpages
- [x] Add Logging
- [x] Set configs in a separate file
- [x] Set limit for saving web pages
- [x] Adding a random time for retrieving the web pages
- [x] Adjustable path to the backup (archive) folder
- [x] Implementation for different operating systems
    - [x] Linux (using cron job)
    - [ ] Windows (using scheduler)
    - [ ] Using Docker
- [ ] Parallelize the web requests
- [ ] Send regular summaries as emails
