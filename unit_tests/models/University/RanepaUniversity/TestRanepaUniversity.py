from typing import List
from werkzeug.exceptions import NotFound, BadRequest
from models.Program.implementations.RanepaProgram import RanepaProgram
from unit_tests.models.University.RanepaUniversity.parser import test_parser
from models.University.implementations import RanepaUniversity
import unittest
from parsing_module.parsers import ranepa_parser


def programs_generator(quantity: int) -> List[RanepaProgram]:
    result = list()

    for i in range(0, quantity):
        result.append(RanepaProgram(f"Departament{i}", f"Approval{i}", f"Form{i}", f"Program{i}"))

    return result


class TestRanepaUniversity(unittest.TestCase):
    def setUp(self):
        RanepaUniversity.parser = test_parser

    def test_get_position_should_throw_exception_when_programs_list_contain_not_existing_program(self):
        programs = programs_generator(5)
        programs.append(RanepaProgram("Not existing departament", "Not existing approval",
                                      "Not existing form", "Not existing program"))

        ranepa = RanepaUniversity.RanepaUniversity(programs)

        self.assertRaises(NotFound, ranepa.get_position, "Name", "Surname", "Lastname")

    def test_get_position_should_throw_exception_when_student_is_not_exist(self):
        programs = programs_generator(3)

        ranepa = RanepaUniversity.RanepaUniversity(programs)

        self.assertRaises(NotFound, ranepa.get_position, "Notexistingname", "Notexistingsurname", "Notexistinglastname")

    def test_get_position_should_throw_exception_when_site_is_not_available(self):
        programs = programs_generator(5)
        programs.append(RanepaProgram("Bad request", "Bad request", "Bad request", "Bad request"))

        ranepa = RanepaUniversity.RanepaUniversity(programs)

        self.assertRaises(BadRequest, ranepa.get_position, "Name", "Surname", "Lastname")

    def test_get_position_should_works_correctly_when_programs_list_is_empty(self):
        programs = programs_generator(0)

        ranepa = RanepaUniversity.RanepaUniversity(programs)

        self.assertListEqual(ranepa.get_position("Name", "Surname", "Lastname"), list())

    def test_get_position_should_works_correctly_when_programs_list_contain_one_element(self):
        programs = programs_generator(1)

        ranepa = RanepaUniversity.RanepaUniversity(programs)

        result = [(RanepaProgram("Departament0", "Approval0", "Form0", "Program0"), 10)]

        self.assertListEqual(ranepa.get_position("Name", "Surname", "Lastname"), result)

    def test_get_position_should_works_correctly_when_programs_list_contain_many_elements(self):
        programs = programs_generator(100)

        ranepa = RanepaUniversity.RanepaUniversity(programs)

        result = list()
        for i in range(0, 100):
            result.append((programs[i], 10))

        self.assertListEqual(ranepa.get_position("Name", "Surname", "Lastname"), result)

    def tearDown(self):
        RanepaUniversity.parser = ranepa_parser


if __name__ == '__main__':
    unittest.main()
