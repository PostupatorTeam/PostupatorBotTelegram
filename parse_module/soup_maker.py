import ssl
from time import sleep
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


def make_soup(url: str) -> BeautifulSoup:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    request = Request(url, headers=headers)

    time = 0
    while time < 3:
        try:
            html = urlopen(request, context=ssl.SSLContext(ssl.PROTOCOL_SSLv23)).read().decode("utf-8")

            return BeautifulSoup(html, "html.parser")
        except (HTTPError, URLError):
            time += 1
            sleep(1)

    raise Exception("Can not access to site.")
