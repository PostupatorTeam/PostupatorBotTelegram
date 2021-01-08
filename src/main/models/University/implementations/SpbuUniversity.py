import logging
from typing import List, Tuple
from werkzeug.exceptions import BadRequest
from src.main.models.Program.implementations.SpbuProgram import SpbuProgram
from src.main.models.University.interface.University import University
from src.main.parsing_module.parsers import spbu_parser

parser = spbu_parser


class SpbuUniversity(University):
    programs: List[SpbuProgram]

    def __init__(self, programs: List[SpbuProgram]):
        self.programs = programs

    def get_position(self, name: str, surname: str, lastname: str) -> List[Tuple[SpbuProgram, int]]:
        result = list()

        for program in self.programs:
            try:
                result.append(parser.get_position(name, surname, lastname, program))
            except BadRequest:
                message = "Failure to connect to the Spbu university site was detecting in SpbuUniversity class."
                logging.warning(message)
                raise BadRequest("Не удалось подключиться к сайту университета СПБГУ.")

        return result
