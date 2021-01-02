from dataclasses import dataclass
from typing import Tuple, List
from models.ConcreteUniversityStudent.interface.ConcreteUniversityStudent import ConcreteUniversityStudent
from models.Program.implementations.SpbuProgram import SpbuProgram


@dataclass
class SpbuStudent(ConcreteUniversityStudent):
    id: str
    name: str
    surname: str
    lastname: str
    programs: List[Tuple[SpbuProgram, int]]
