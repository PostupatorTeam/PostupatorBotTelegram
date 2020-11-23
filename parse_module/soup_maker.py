from time import sleep
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from requests_html import HTMLSession


def make_soup(url: str, js: bool) -> BeautifulSoup:
    time = 0

    while time < 3:
        try:
            response = HTMLSession().get(url)

            if js:
                response.html.render()

            return BeautifulSoup(str(response.html.element), "html.parser")
        except (HTTPError, URLError):
            time += 1
            sleep(1)

    raise Exception("Can not access to site.")
