import soup_maker

main_link = "https://ssau.ru/ratings/bakalavr"


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
    soup = soup_maker.make_soup(link, True)

    for tr in soup.find_all("table")[1].find_all("tbody")[0].find_all("tr"):
        tds = tr.find_all("td")

        if len(tds) > 0 and tds[1].text.replace("\t", "").replace("\n", "").replace(" ", "") == student.surname + student.name + student.lastname:
            return int(tds[0].text)

    raise Exception("")


def get_link_to_table(program: Program) -> str:
    link = "http://apply.rggu.ru/baccalaureate_list_budget/#5aae2cc7014e81edaccbece9c442ef0d"

    return link
