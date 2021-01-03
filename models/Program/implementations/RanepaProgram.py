from dataclasses import dataclass
from models.Program.interface.Program import Program


@dataclass
class RanepaProgram(Program):
    departament: str
    approval: str
    form: str
    program: str

    def __str__(self) -> str:
        return f"{self.departament}/{self.approval}/{self.form}/{self.program}"
