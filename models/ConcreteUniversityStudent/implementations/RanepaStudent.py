from dataclasses import dataclass
from typing import Tuple, List
from models.ConcreteUniversityStudent.interface.ConcreteUniversityStudent import ConcreteUniversityStudent
from models.Program.implementations.RanepaProgram import RanepaProgram


@dataclass
class RanepaStudent(ConcreteUniversityStudent):
    userid: str
    name: str
    surname: str
    lastname: str
    programs: List[Tuple[RanepaProgram, int]]
