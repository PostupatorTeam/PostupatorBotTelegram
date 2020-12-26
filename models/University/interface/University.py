from interface import Interface


class University(Interface):
    programs: list

    def get_position(self, name: str, surname: str, lastname: str) -> list:
        pass
