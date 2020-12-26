from dataclasses import dataclass
from interface import implements
from models.ConcreteUniversityStudent.interface import ConcreteUniversityStudent


@dataclass
class SpbuStudent(implements(ConcreteUniversityStudent)):
    id: str
    name: str
    surname: str
    lastname: str
    programs: list
