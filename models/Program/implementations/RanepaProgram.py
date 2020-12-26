from dataclasses import dataclass
from interface import implements
from models.Program.interface import Program


@dataclass
class RanepaProgram(implements(Program)):
    departament: str
    approval: str
    form: str
    program: str
