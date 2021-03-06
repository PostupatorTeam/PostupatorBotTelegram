import logging
from typing import List, Tuple
from werkzeug.exceptions import BadRequest
from src.main.models.Program.implementations.EtuProgram import EtuProgram
from src.main.models.University.interface.University import University
from src.main.parsing_module.parsers import etu_parser

parser = etu_parser


class EtuUniversity(University):
    programs: List[EtuProgram]

    def __init__(self, programs: List[EtuProgram]):
        self.programs = programs

    def get_position(self, name: str, surname: str, lastname: str) -> List[Tuple[EtuProgram, int]]:
        result = list()

        for program in self.programs:
            try:
                result.append(parser.get_position(name, surname, lastname, program))
            except BadRequest:
                message = "Failure to connect to the Etu university site was detecting in EtuUniversity class."
                logging.warning(message)
                raise BadRequest("Не удалось подключиться к сайту университета ЛЭТИ.")

        return result
