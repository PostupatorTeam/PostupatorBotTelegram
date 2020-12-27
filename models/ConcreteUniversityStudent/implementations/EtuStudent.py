from dataclasses import dataclass
from typing import Tuple, List
from interface import implements
from models.ConcreteUniversityStudent.interface import ConcreteUniversityStudent
from models.Program.implementations.EtuProgram import EtuProgram


@dataclass
class EtuStudent(implements(ConcreteUniversityStudent)):
    id: str
    name: str
    surname: str
    lastname: str
    programs: List[Tuple[EtuProgram, int]]
