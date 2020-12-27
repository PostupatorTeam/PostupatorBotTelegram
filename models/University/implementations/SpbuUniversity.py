import logging
from typing import List, Tuple
from interface import implements
from werkzeug.exceptions import BadRequest, NotFound
from models.Program.implementations.SpbuProgram import SpbuProgram
from models.University.interface import University


def get_position_for_current_program(name: str, surname: str, lastname: str, program: SpbuProgram) -> \
        Tuple[SpbuProgram, int]:
    # InternalError
    pass


class SpbuUniversity(implements(University)):
    programs: List[SpbuProgram]

    def __init__(self, programs: List[SpbuProgram]):
        self.programs = programs

    def get_position(self, name: str, surname: str, lastname: str) -> List[Tuple[SpbuProgram, int]]:
        result = list()

        for program in self.programs:
            try:
                result.append(get_position_for_current_program(name, surname, lastname, program))
            except BadRequest:
                message = "Failure to connect to the Spbu university site was detecting in SpbuUniversity class."
                logging.warning(message)
                raise BadRequest("Не удалось подключиться к сайту университета РАНХИГС.")

            return result
