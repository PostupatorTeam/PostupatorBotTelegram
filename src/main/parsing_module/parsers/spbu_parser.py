import logging
from typing import Tuple
from werkzeug.exceptions import NotFound
from config import config
from src.main.models.Program.implementations.SpbuProgram import SpbuProgram
from src.main.parsing_module.make_soup import make_soup


def program_name_compare(program_name: str, data_from_site: str) -> bool:
    index = 0
    for i in range(0, len(data_from_site)):
        if data_from_site[i] == ' ':
            index = i
            break
    return program_name == data_from_site[index + 1::]


def educational_form_compare(educational_form_name: str, data_from_site: str) -> bool:
    return f"Форма обучения: {educational_form_name}" == data_from_site


def get_link_to_table(program: SpbuProgram) -> str:
    soup = make_soup(config.spbu_link_to_list, False)

    program_found = False
    form_found = False
    for item in soup.find_all(["a", "b"]):
        if program_found and form_found:
            if item.has_attr("href"):
                if item.string.strip() == program.pay_form:
                    return item["href"]
            else:
                break
        elif program_found:
            if item.name == "b" and not item.has_attr("style"):
                if educational_form_compare(program.educational_form, item.string.strip()):
                    form_found = True
                    continue
            elif item.name == "b":
                break
        else:
            if item.name == "b" and item.has_attr("style"):
                if program_name_compare(program.program, item.string.strip()):
                    program_found = True
                    continue

    message = \
        f"Failure to find educational program {str(program)} " \
        f"on the Spbu university site was detecting in SpbuUniversity class."
    logging.warning(message)
    message = \
        f"Не удалось найти образовательную программу {str(program)} на сайте университета СПБГУ."
    raise NotFound(message)


def get_position(name: str, surname: str, lastname: str, program: SpbuProgram) -> Tuple[SpbuProgram, int]:
    soup = make_soup(f"{config.spbu_base_link}{get_link_to_table(program)}", False)

    for tr in soup.find_all("table")[0].find_all("tbody")[0].find_all("tr"):
        tds = tr.find_all("td")

        place = tds[0].string.strip()
        fio = tds[2].text.strip()

        if fio == f"{surname} {name} {lastname}":
            return program, int(place)

    message = \
        f"Failure to find student with this name on the Spbu university site was detecting in SpbuUniversity class."
    logging.warning(message)
    message = \
        f"Не удалось найти абитуриента с такими данными в таблице {str(program)} на сайте университета СПБГУ."
    raise NotFound(message)
