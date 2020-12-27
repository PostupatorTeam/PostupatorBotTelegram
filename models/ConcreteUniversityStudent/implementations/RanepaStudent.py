from dataclasses import dataclass
from typing import Tuple, List
from interface import implements
from models.ConcreteUniversityStudent.interface import ConcreteUniversityStudent
from models.Program.implementations.RanepaProgram import RanepaProgram


@dataclass
class RanepaStudent(implements(ConcreteUniversityStudent)):
    id: str
    name: str
    surname: str
    lastname: str
    programs: List[Tuple[RanepaProgram, int]]
