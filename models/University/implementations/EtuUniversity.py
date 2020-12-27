import logging
from typing import List, Tuple
from interface import implements
from werkzeug.exceptions import BadRequest, NotFound
from config import config
from models.Program.implementations.EtuProgram import EtuProgram
from models.University.interface import University
from parsing_module.parsing_module import make_soup


def get_link_to_table(program: EtuProgram) -> str:
    link = config.etu_base_link

    soup = make_soup(config.etu_link_to_list, False)

    for tr in soup.find_all("table")[0].find_all("tbody")[0].find_all("tr"):
        program_name = tr.find_all("td")[1].string

        if program_name == program.program:
            if program.form == "Бюджет":
                link += tr.find_all("td")[2].find_all("a")[0]["href"]
                return link
            elif program.form == "Коммерция":
                link += tr.find_all("td")[3].find_all("a")[0]["href"]
                return link

    message = \
        f"Failure to find educational program {str(program)} " \
        f"on the Etu university site was detecting in EtuUniversity class."
    logging.warning(message)
    message = \
        f"Не удалось найти образовательную программу {str(program)} на сайте университета ЛЭТИ."
    raise NotFound(message)


def get_position_for_current_program(name: str, surname: str, lastname: str, program: EtuProgram) -> \
        Tuple[EtuProgram, int]:
    link = get_link_to_table(program)
    soup = make_soup(link, False)

    for tr in soup.find_all("table")[0].find_all("tbody")[0].find_all("tr"):
        for td in tr.find_all("td"):
            place = 0

            if td["class"][0] == "number":
                place = td.string.strip()

            if td["class"][0] == "fio":
                if td.string.strip() == f"{surname} {name} {lastname}":
                    return program, int(place)

    message = \
        f"Failure to find student with this name on the Etu university site was detecting in EtuUniversity class."
    logging.warning(message)
    message = \
        f"Не удалось найти абитуриента с такими данными в таблице {str(program)} на сайте университета РАНХИГС."
    raise NotFound(message)


class EtuUniversity(implements(University)):
    programs: List[EtuProgram]

    def __init__(self, programs: List[EtuProgram]):
        self.programs = programs

    def get_position(self, name: str, surname: str, lastname: str) -> List[Tuple[EtuProgram, int]]:
        result = list()

        for program in self.programs:
            try:
                result.append(get_position_for_current_program(name, surname, lastname, program))
            except BadRequest:
                message = "Failure to connect to the Etu university site was detecting in EtuUniversity class."
                logging.warning(message)
                raise BadRequest("Не удалось подключиться к сайту университета ЛЭТИ.")

        return result
