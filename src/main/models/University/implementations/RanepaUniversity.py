import logging
from typing import List, Tuple
from werkzeug.exceptions import BadRequest
from src.main.models.Program.implementations.RanepaProgram import RanepaProgram
from src.main.models.University.interface.University import University
from src.main.parsing_module.parsers import ranepa_parser

parser = ranepa_parser


class RanepaUniversity(University):
    programs: List[RanepaProgram]

    def __init__(self, programs: List[RanepaProgram]):
        self.programs = programs

    def get_position(self, name: str, surname: str, lastname: str) -> List[Tuple[RanepaProgram, int]]:
        result = list()

        for program in self.programs:
            try:
                result.append(parser.get_position(name, surname, lastname, program))
            except BadRequest:
                message = "Failure to connect to the Ranepa university site was detecting in RanepaUniversity class."
                logging.warning(message)
                raise BadRequest("Не удалось подключиться к сайту университета РАНХИГС.")

        return result
