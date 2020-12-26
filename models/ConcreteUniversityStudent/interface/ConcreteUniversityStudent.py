from interface import Interface


class ConcreteUniversityStudent(Interface):
    id: str
    name: str
    surname: str
    lastname: str
    programs: list
