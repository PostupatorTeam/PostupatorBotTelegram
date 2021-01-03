from dataclasses import dataclass
from models.Program.interface.Program import Program


@dataclass
class SpbuProgram(Program):
    educational_form: str
    pay_form: str
    program: str

    def __str__(self) -> str:
        return f"{self.program}/{self.educational_form}/{self.pay_form}"
