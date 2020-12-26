from interface import implements
from models.University.interface import University


class EtuUniversity(implements(University)):
    programs: list

    def get_position(self, name: str, surname: str, lastname: str) -> list:
        pass
