from dataclasses import dataclass
from models.Program.interface.Program import Program


@dataclass
class EtuProgram(Program):
    form: str
    program: str

    def __str__(self) -> str:
        return f"{self.form}/{self.program}"
