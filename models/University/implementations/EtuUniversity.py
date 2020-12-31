import logging
from typing import List, Tuple
from interface import implements
from werkzeug.exceptions import BadRequest
from models.Program.implementations.EtuProgram import EtuProgram
from models.University.interface import University
from parsing_module.parsers import etu_parser


parser = etu_parser


class EtuUniversity(implements(University)):
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
