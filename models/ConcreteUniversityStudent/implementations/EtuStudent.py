from dataclasses import dataclass
from interface import implements
from models.ConcreteUniversityStudent.interface import ConcreteUniversityStudent


@dataclass
class EtuStudent(implements(ConcreteUniversityStudent)):
    id: str
    name: str
    surname: str
    lastname: str
    programs: list
