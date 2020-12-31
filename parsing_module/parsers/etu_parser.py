import logging
from typing import Tuple
from werkzeug.exceptions import NotFound
from config import config
from models.Program.implementations.EtuProgram import EtuProgram
from parsing_module.make_soup import make_soup


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


def get_position(name: str, surname: str, lastname: str, program: EtuProgram) -> Tuple[EtuProgram, int]:
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
