from dataclasses import dataclass

import soup_maker


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


# strip()
def html_string_to_simple_string(string: str) -> str:
    return string.replace("\t", "").replace("\n", "").replace(" ", "")


def get_position(student: Student) -> int:
    link = get_link_to_table(student.program)
    soup = soup_maker.make_soup(link, True)

    for tr in soup.find_all("table")[0].find_all("tbody")[0].find_all("tr"):
        tds = tr.find_all("td")

        if html_string_to_simple_string(tds[1].text) == student.surname + student.name + student.lastname:
            return int(html_string_to_simple_string(tds[0].text))

    raise Exception("Can not find student with this data.")


def get_link_to_table(program: Program) -> str:
    soup = soup_maker.make_soup("https://ssau.ru/ratings/bakalavr", True)
    link = "http://ssau.ru"

    for div in soup.find_all("div"):
        if div.has_attr("class") and div["class"] == "card-body d-flex flex-column flex-lg-row":
            a = div.find_all("div")[0].find_all("h5")[0].find_all("a")[0]
            form = html_string_to_simple_string(div.find_all("div")[1].find_all("div")[0].find_all("div")[1].text)

            if html_string_to_simple_string(a.string) == program.program and form == program.form:
                link += a["href"]
                break

    soup = soup_maker.make_soup(link, True)

    for a in soup.find_all("nav")[0].find_all("a"):
        if html_string_to_simple_string(a.string) == program.form:
            return link + a["href"]

    raise Exception("Can not find educational program with this data.")
