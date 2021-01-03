from abc import ABCMeta
from typing import Tuple, List
from models.Program.interface.Program import Program


class ConcreteUniversityStudent:
    __metaclass__ = ABCMeta

    id: str
    name: str
    surname: str
    lastname: str
    programs: List[Tuple[Program, int]]
