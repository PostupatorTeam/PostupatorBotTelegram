from typing import List, Tuple
from interface import Interface
from models.Program.interface.Program import Program


class University(Interface):
    programs: List[Program]

    def get_position(self, name: str, surname: str, lastname: str) -> List[Tuple[Program, int]]:
        pass
