from dataclasses import dataclass
from typing import Tuple, List
from models.ConcreteUniversityStudent.interface.ConcreteUniversityStudent import ConcreteUniversityStudent
from models.Program.implementations.EtuProgram import EtuProgram


@dataclass
class EtuStudent(ConcreteUniversityStudent):
    id: str
    name: str
    surname: str
    lastname: str
    programs: List[Tuple[EtuProgram, int]]
