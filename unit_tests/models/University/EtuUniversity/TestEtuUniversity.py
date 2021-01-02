from typing import List
from werkzeug.exceptions import NotFound, BadRequest
from models.Program.implementations.EtuProgram import EtuProgram
from unit_tests.models.University.EtuUniversity.parser import test_parser
from models.University.implementations import EtuUniversity
import unittest
from parsing_module.parsers import etu_parser


def programs_generator(quantity: int) -> List[EtuProgram]:
    result = list()

    for i in range(0, quantity):
        result.append(EtuProgram(f"Form{i}", f"Program{i}"))

    return result


class TestEtuUniversity(unittest.TestCase):
    def setUp(self):
        EtuUniversity.parser = test_parser

    def test_get_position_should_throw_exception_when_programs_list_contain_not_existing_program(self):
        programs = programs_generator(5)
        programs.append(EtuProgram("Not existing form", "Not existing program"))

        etu = EtuUniversity.EtuUniversity(programs)

        self.assertRaises(NotFound, etu.get_position, "Name", "Surname", "Lastname")

    def test_get_position_should_throw_exception_when_student_is_not_exist(self):
        programs = programs_generator(3)

        etu = EtuUniversity.EtuUniversity(programs)

        self.assertRaises(NotFound, etu.get_position, "Notexistingname", "Notexistingsurname", "Notexistinglastname")

    def test_get_position_should_throw_exception_when_site_is_not_available(self):
        programs = programs_generator(5)
        programs.append(EtuProgram("Bad request", "Bad request"))

        etu = EtuUniversity.EtuUniversity(programs)

        self.assertRaises(BadRequest, etu.get_position, "Name", "Surname", "Lastname")

    def test_get_position_should_works_correctly_when_programs_list_is_empty(self):
        programs = programs_generator(0)

        etu = EtuUniversity.EtuUniversity(programs)

        self.assertListEqual(etu.get_position("Name", "Surname", "Lastname"), list())

    def test_get_position_should_works_correctly_when_programs_list_contain_one_element(self):
        programs = programs_generator(1)

        etu = EtuUniversity.EtuUniversity(programs)

        result = [(EtuProgram("Form0", "Program0"), 10)]

        self.assertListEqual(etu.get_position("Name", "Surname", "Lastname"), result)

    def test_get_position_should_works_correctly_when_programs_list_contain_many_elements(self):
        programs = programs_generator(100)

        etu = EtuUniversity.EtuUniversity(programs)

        result = list()
        for i in range(0, 100):
            result.append((programs[i], 10))

        self.assertListEqual(etu.get_position("Name", "Surname", "Lastname"), result)

    def tearDown(self):
        EtuUniversity.parser = etu_parser


if __name__ == '__main__':
    unittest.main()
