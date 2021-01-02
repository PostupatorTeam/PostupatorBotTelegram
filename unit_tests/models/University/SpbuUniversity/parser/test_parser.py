from typing import Tuple
from werkzeug.exceptions import NotFound, BadRequest
from models.Program.implementations.SpbuProgram import SpbuProgram


def get_position(name: str, surname: str, lastname: str, program: SpbuProgram) -> Tuple[SpbuProgram, int]:
    if program == SpbuProgram("Not existing educational form", "Not existing pay form", "Not existing program"):
        raise NotFound()

    if name == "Notexistingname" and surname == "Notexistingsurname" and lastname == "Notexistinglastname":
        raise NotFound()

    if program == SpbuProgram("Bad request", "Bad request", "Bad request"):
        raise BadRequest()

    return program, 10
