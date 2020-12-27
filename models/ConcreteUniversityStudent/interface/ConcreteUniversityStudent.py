from typing import Tuple, List
from interface import Interface
from models.Program.interface.Program import Program


class ConcreteUniversityStudent(Interface):
    id: str
    name: str
    surname: str
    lastname: str
    programs: List[Tuple[Program, int]]
