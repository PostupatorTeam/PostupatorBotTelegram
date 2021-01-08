from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


@dataclass
class Program:
    pay_form: Optional[str]
    educational_form: Optional[str]
    approval: Optional[str]
    program: Optional[str]
    university_branch: Optional[str]
    university_name: Optional[str]


@dataclass
class Student:
    name: Optional[str]
    surname: Optional[str]
    lastname: Optional[str]
    programs: List[Program]
    is_registered: bool
    is_added_program: bool


class RegistrationData(Enum):
    Empty = 0
    Name = 1
    Surname = 2
    Patronymic = 3
    University_Name = 4
    Program_Info = 5
    End = 6
