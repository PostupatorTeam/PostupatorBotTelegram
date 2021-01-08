from dataclasses import dataclass
from typing import List
from src.main.models.University.interface.University import University


@dataclass
class Student:
    userid: str
    name: str
    surname: str
    lastname: str
    universities: List[University]
