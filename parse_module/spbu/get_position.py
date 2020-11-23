import soup_maker
from requests_html import HTMLSession

main_link = "https://etu.ru/ru/abiturientam/priyom-na-1-y-kurs/podavshie-zayavlenie/"


class Program:
    departament: str
    approval: str
    form: str
    program: str


class Student:
    name: str
    surname: str
    lastname: str
    program: Program


def add_link_element(link: str, elem: str) -> str:
    soup = soup_maker.make_soup(link, False)

    for a in soup.find_all("table")[0].find_all("tbody")[0].find_all("a"):
        if a.string.replace("\t", "").replace("\n", "").replace(" ", "") == elem:
            return a["href"]

    raise Exception("")


def get_position(student: Student) -> int:
    link = get_link_to_table(student.program)
    soup = soup_maker.make_soup(link, False)

    for tr in soup.find_all("table")[0].find_all("tbody")[0].find_all("tr"):
        tds = tr.find_all("td")
        if tds[2].text.replace("\t", "").replace("\n", "").replace(" ", "") == student.surname + student.name + student.lastname:
            return int(tds[0].text)

    raise Exception("")


def get_link_to_table(program: Program):
    link = "https://cabinet.spbu.ru/Lists/1k_EntryLists/index_comp_groups.html"

    response = HTMLSession().get(link)

    return response
