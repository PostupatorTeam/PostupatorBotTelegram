from dataclasses import dataclass
from interface import implements
from models.Program.interface import Program


@dataclass
class SpbuProgram(implements(Program)):
    educational_form: str
    pay_form: str
    program: str
