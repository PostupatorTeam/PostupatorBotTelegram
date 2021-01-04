from dataclasses import dataclass
from typing import List
from models.University.interface.University import University


@dataclass
class Student:
    userid: str
    name: str
    surname: str
    lastname: str
    universities: List[University]
