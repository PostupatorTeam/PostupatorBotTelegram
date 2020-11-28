from dataclasses import dataclass
from Models.universityModel import Program

@dataclass
class Student:
    name: str
    surname: str
    lastname: str
    program: Program