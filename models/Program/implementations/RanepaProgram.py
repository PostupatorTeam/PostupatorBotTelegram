from dataclasses import dataclass
from interface import implements
from models.Program.interface import Program


@dataclass
class RanepaProgram(implements(Program)):
    departament: str
    approval: str
    form: str
    program: str

    def __str__(self) -> str:
        return f"{self.departament}/{self.approval}/{self.form}/{self.program}"
