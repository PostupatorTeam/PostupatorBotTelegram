from typing import Tuple
from werkzeug.exceptions import NotFound, BadRequest
from models.Program.implementations.EtuProgram import EtuProgram


def get_position(name: str, surname: str, lastname: str, program: EtuProgram) -> Tuple[EtuProgram, int]:
    if program == EtuProgram("Not existing form", "Not existing program"):
        raise NotFound()

    if program == EtuProgram("Bad request", "Bad request"):
        raise BadRequest()

    if name == "Notexistingname" and surname == "Notexistingsurname" and lastname == "Notexistinglastname":
        raise NotFound()

    return program, 10
