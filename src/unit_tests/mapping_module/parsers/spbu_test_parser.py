from typing import Tuple
from werkzeug.exceptions import NotFound, BadRequest
from src.main.models.Program.implementations.SpbuProgram import SpbuProgram


def get_position(name: str, surname: str, lastname: str, program: SpbuProgram) -> Tuple[SpbuProgram, int]:
    if name == "Notexistingname" and surname == "Notexistingsurname" and lastname == "Notexistinglastname":
        raise NotFound()

    if program == SpbuProgram("Bad request", "Bad request", "Bad request"):
        raise BadRequest()

    return program, 10
