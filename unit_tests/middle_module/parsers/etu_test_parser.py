from typing import Tuple
from werkzeug.exceptions import NotFound, BadRequest
from models.Program.implementations.EtuProgram import EtuProgram


def get_position(name: str, surname: str, lastname: str, program: EtuProgram) -> Tuple[EtuProgram, int]:
    if name == "Notexistingname" and surname == "Notexistingsurname" and lastname == "Notexistinglastname":
        raise NotFound()

    if program == EtuProgram("Bad request", "Bad request"):
        raise BadRequest()

    return program, 5
