from dataclasses import dataclass
from typing import Tuple, List
from src.main.models.ConcreteUniversityStudent.interface.ConcreteUniversityStudent import ConcreteUniversityStudent
from src.main.models.Program.implementations.EtuProgram import EtuProgram


@dataclass
class EtuStudent(ConcreteUniversityStudent):
    userid: str
    name: str
    surname: str
    lastname: str
    programs: List[Tuple[EtuProgram, int]]
