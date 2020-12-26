from dataclasses import dataclass
from interface import implements
from models.Program.interface import Program


@dataclass
class EtuProgram(implements(Program)):
    form: str
    program: str
