from dataclasses import dataclass
import soup_maker


@dataclass
class Program:
    form: str
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
        for td in tr.find_all("td"):
            number = 0

            if td["class"][0] == "number":
                number = td.string.strip()

            if td["class"][0] == "fio":
                if td.string.strip() == f"{student.surname} + {student.name} + {student.lastname}":
                    return int(number)

    raise Exception("Can not find student with this data.")


def get_link_to_table(program: Program) -> str:
    link = "https://etu.ru/"

    soup = soup_maker.make_soup("https://etu.ru/ru/abiturientam/priyom-na-1-y-kurs/podavshie-zayavlenie/", False)

    for tr in soup.find_all("table")[0].find_all("tbody")[0].find_all("tr"):
        program_name = tr.find_all("td")[1].string

        if program_name == program.program:
            if program.form == "Бюджет":
                link += tr.find_all("td")[2].find_all("a")[0]["href"]
                return link
            if program.form == "Коммерция":
                link += tr.find_all("td")[3].find_all("a")[0]["href"]
                return link

    raise Exception("Can not find educational program with this data.")
