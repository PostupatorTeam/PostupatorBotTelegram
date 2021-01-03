import logging
from time import sleep
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from werkzeug.exceptions import BadRequest


def make_soup(link: str, js: bool) -> BeautifulSoup:
    time = 0

    while time < 3:
        try:
            response = HTMLSession().get(link)

            if js:
                response.html.render()

            return BeautifulSoup(str(response.html.element), "html.parser")
        except (HTTPError, URLError, ConnectionError):
            time += 1
            sleep(1)

    logging.warning("Failure to connect to the site was detecting in parsing module.")
    raise BadRequest()
