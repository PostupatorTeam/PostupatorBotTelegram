import soup_maker

main_link = "https://lk.ranepa.ru/pk/list.php?FT=1&FL=0"


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
    soup = soup_maker.make_soup(link)

    for a in soup.find_all("table")[0].find_all("tbody")[0].find_all("a"):
        if a.string.replace("\t", "").replace("\n", "").replace(" ", "") == elem:
            return a["href"]

    raise Exception("")


def get_position(student: Student) -> int:
    link = get_link_to_table(student.program)
    soup = soup_maker.make_soup(link)

    for tr in soup.find_all("table")[0].find_all("tbody")[0].find_all("tr"):
        tds = tr.find_all("td")

        place = tds[0].string.replace("\t", "").replace("\n", "").replace(" ", "")
        fio = tds[1].find_all("a")[0].string.replace("\t", "").replace("\n", "").replace(" ", "")

        if fio == student.surname + student.name + student.lastname:
            return int(place)

    raise Exception("")


def get_link_to_table(program: Program) -> str:
    link = main_link

    link += add_link_element(link, program.departament.replace(" ", ""))
    link += add_link_element(link, program.approval.replace(" ", ""))
    link += add_link_element(link, program.form.replace(" ", ""))
    link += add_link_element(link, program.program.replace(" ", ""))

    return link
