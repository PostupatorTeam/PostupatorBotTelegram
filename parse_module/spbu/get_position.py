from dataclasses import dataclass

import soup_maker


@dataclass
class Program:
    educational_form: str
    pay_form: str
    program: str


@dataclass
class Student:
    name: str
    surname: str
    lastname: str
    program: Program


def get_position(student: Student) -> int:
    link = get_link_to_table(student.program)
    soup = soup_maker.make_soup(link, False)

    for tr in soup.find_all("table")[0].find_all("tbody")[0].find_all("tr"):
        tds = tr.find_all("td")
        if tds[2].text == f"{student.surname} {student.name} {student.lastname}":
            return int(tds[0].text)

    raise Exception("")


def get_link_to_table(program: Program) -> str:
    link = "https://cabinet.spbu.ru/Lists/1k_EntryLists/list_881c6251-cdbd-4cd8-8e49-8ad40191ce94.html"

    return link
