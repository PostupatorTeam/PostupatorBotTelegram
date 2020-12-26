import soup_maker
from dataclasses import dataclass


@dataclass
class Program:
    departament: str
    approval: str
    form: str
    program: str


@dataclass
class Student:
    name: str
    surname: str
    lastname: str
    program: Program


def add_link_element(link: str, current_element: str) -> str:
    soup = soup_maker.make_soup(link, False)

    for a in soup.find_all("table")[0].find_all("tbody")[0].find_all("a"):
        if a.string.strip() == current_element:
            return a["href"]

    raise Exception("Can not find element with this name.")


def get_link_to_table(program: Program) -> str:
    link = "https://lk.ranepa.ru/pk/list.php?FT=1&FL=0"

    link += add_link_element(link, program.departament)
    link += add_link_element(link, program.approval)
    link += add_link_element(link, program.form)
    link += add_link_element(link, program.program)

    return link


def get_position(student: Student) -> int:
    link = get_link_to_table(student.program)
    soup = soup_maker.make_soup(link, False)

    for tr in soup.find_all("table")[0].find_all("tbody")[0].find_all("tr"):
        tds = tr.find_all("td")

        place = tds[0].string.strip()
        fio = tds[1].find_all("a")[0].string.strip()

        if fio == f"{student.surname} {student.name} {student.lastname}":
            return int(place)

    raise Exception("Can not find student with data.")
