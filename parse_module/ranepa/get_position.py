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


def html_string_to_simple_string(string: str) -> str:
    return string.replace("\t", "").replace("\n", "").replace(" ", "")


def add_link_element(link: str, current_element: str) -> str:
    soup = soup_maker.make_soup(link, False)

    for a in soup.find_all("table")[0].find_all("tbody")[0].find_all("a"):
        if html_string_to_simple_string(a.string) == current_element:
            return a["href"]

    raise Exception("Cannot find element with this name.")


def get_link_to_table(program: Program) -> str:
    link = "https://lk.ranepa.ru/pk/list.php?FT=1&FL=0"

    link += add_link_element(link, program.departament.replace(" ", ""))
    link += add_link_element(link, program.approval.replace(" ", ""))
    link += add_link_element(link, program.form.replace(" ", ""))
    link += add_link_element(link, program.program.replace(" ", ""))

    return link


def get_position(student: Student) -> int:
    link = get_link_to_table(student.program)
    soup = soup_maker.make_soup(link, False)

    for tr in soup.find_all("table")[0].find_all("tbody")[0].find_all("tr"):
        tds = tr.find_all("td")

        place = html_string_to_simple_string(tds[0].string)
        fio = html_string_to_simple_string(tds[1].find_all("a")[0].string)

        if fio == student.surname + student.name + student.lastname:
            return int(place)

    raise Exception("Can not find student with data.")
