from abc import ABCMeta, abstractmethod
from typing import List, Tuple
from models.Program.interface.Program import Program


class University:
    __metaclass__ = ABCMeta

    programs: List[Program]

    @abstractmethod
    def get_position(self, name: str, surname: str, lastname: str) -> List[Tuple[Program, int]]:
        pass
