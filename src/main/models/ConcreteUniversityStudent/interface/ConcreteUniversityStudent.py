from abc import ABCMeta
from typing import Tuple, List
from src.main.models.Program.interface.Program import Program


class ConcreteUniversityStudent:
    __metaclass__ = ABCMeta

    userid: str
    name: str
    surname: str
    lastname: str
    programs: List[Tuple[Program, int]]
