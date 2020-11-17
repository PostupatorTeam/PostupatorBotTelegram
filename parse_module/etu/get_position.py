import soup_maker

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
    soup = soup_maker.make_soup(link)

    for a in soup.find_all("table")[0].find_all("tbody")[0].find_all("a"):
        if a.string.replace("\t", "").replace("\n", "").replace(" ", "") == elem:
            return a["href"]

    raise Exception("")


def get_position(student: Student) -> int:
    link = get_link_to_table(student.program)
    soup = soup_maker.make_soup(link)

    for tr in soup.find_all("table")[0].find_all("tbody")[0].find_all("tr"):
        for td in tr.find_all("td"):
            number = 0

            if td["class"][0].replace("\t", "").replace("\n", "").replace(" ", "") == "number":
                number = td.string.replace("\t", "").replace("\n", "").replace(" ", "")

            if td["class"][0] == "fio":
                st = td.string.replace("\t", "").replace("\n", "").replace(" ", "")
                fio = student.surname + student.name + student.lastname
                if st == fio:
                    return int(number)

    raise Exception("")


def get_link_to_table(program: Program) -> str:
    link = "https://etu.ru/"

    soup = soup_maker.makeSoup(main_link)
    for table in soup.find_all("table"):
        if table.has_attr("class"):
            for tbody in table.find_all("tbody"):
                for tr in tbody.find_all("tr"):
                    programName = tr.find_all("td")[1].string
                    print(programName)
                    if programName == program.program:
                        if program.form == "Бюджет":
                            list = tr.find_all("td")[2].find_all("a")[0]["href"]
                            link += list
                            return link
                        else:
                            list = tr.find_all("td")[3].find_all("a")[0]["href"]
                            link += list
                            return link

    return link
