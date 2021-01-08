from typing import Tuple
from werkzeug.exceptions import NotFound, BadRequest
from src.main.models.Program.implementations.RanepaProgram import RanepaProgram


def get_position(name: str, surname: str, lastname: str, program: RanepaProgram) -> Tuple[RanepaProgram, int]:
    if program == RanepaProgram("Not existing departament", "Not existing approval",
                                "Not existing form", "Not existing program"):
        raise NotFound()

    if name == "Notexistingname" and surname == "Notexistingsurname" and lastname == "Notexistinglastname":
        raise NotFound()

    if program == RanepaProgram("Bad request", "Bad request", "Bad request", "Bad request"):
        raise BadRequest()

    return program, 10
