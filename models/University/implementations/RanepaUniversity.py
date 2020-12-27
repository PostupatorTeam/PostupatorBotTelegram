import logging
from typing import List, Tuple
from interface import implements
from werkzeug.exceptions import BadRequest, NotFound
from config import config
from models.Program.implementations.RanepaProgram import RanepaProgram
from models.University.interface import University
from parsing_module.parsing_module import make_soup


def add_link_element(link: str, current_element: str) -> str:
    soup = make_soup(link, False)

    for a in soup.find_all("table")[0].find_all("tbody")[0].find_all("a"):
        if a.string.strip() == current_element:
            return a["href"]

    raise NotFound()


def get_link_to_table(program: RanepaProgram) -> str:
    link = config.ranepa_base_link

    try:
        link += add_link_element(link, program.departament)
        link += add_link_element(link, program.approval)
        link += add_link_element(link, program.form)
        link += add_link_element(link, program.program)
    except NotFound:
        message = \
            f"Failure to find educational program {str(program)} " \
            f"on the Ranepa university site was detecting in RanepaUniversity class."
        logging.warning(message)
        message = \
            f"Не удалось найти образовательную программу {str(program)} на сайте университета РАНХИГС."
        raise NotFound(message)

    return link


def get_position_for_current_program(name: str, surname: str, lastname: str, program: RanepaProgram) -> \
        Tuple[RanepaProgram, int]:
    link = get_link_to_table(program)
    soup = make_soup(link, False)

    for tr in soup.find_all("table")[0].find_all("tbody")[0].find_all("tr"):
        tds = tr.find_all("td")

        place = tds[0].string.strip()
        fio = tds[1].find_all("a")[0].string.strip()

        if fio == f"{surname} {name} {lastname}":
            return program, place

    message = \
        f"Failure to find student with this name on the Ranepa university site was detecting in RanepaUniversity class."
    logging.warning(message)
    message = \
        f"Не удалось найти абитуриента с такими данными в таблице {str(program)} на сайте университета РАНХИГС."
    raise NotFound(message)


class RanepaUniversity(implements(University)):
    programs: List[RanepaProgram]

    def __init__(self, programs: List[RanepaProgram]):
        self.programs = programs

    def get_position(self, name: str, surname: str, lastname: str) -> List[Tuple[RanepaProgram, int]]:
        result = list()

        for program in self.programs:
            try:
                result.append(get_position_for_current_program(name, surname, lastname, program))
            except BadRequest:
                message = "Failure to connect to the Ranepa university site was detecting in RanepaUniversity class."
                logging.warning(message)
                raise BadRequest("Не удалось подключиться к сайту университета РАНХИГС.")

            return result
