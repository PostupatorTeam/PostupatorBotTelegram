from typing import List
from werkzeug.exceptions import NotFound, BadRequest
from src.main.models.Program.implementations.SpbuProgram import SpbuProgram
from src.unit_tests.models.University.SpbuUniversity.parser import test_parser
from src.main.models.University.implementations import SpbuUniversity
import unittest
from src.main.parsing_module.parsers import spbu_parser


def programs_generator(quantity: int) -> List[SpbuProgram]:
    result = list()

    for i in range(0, quantity):
        result.append(SpbuProgram(f"EducationalForm{i}", f"PayForm{i}", f"Program{i}"))

    return result


class TestRanepaUniversity(unittest.TestCase):
    def setUp(self):
        SpbuUniversity.parser = test_parser

    def test_get_position_should_throw_exception_when_programs_list_contain_not_existing_program(self):
        programs = programs_generator(5)
        programs.append(SpbuProgram("Not existing educational form", "Not existing pay form", "Not existing program"))

        spbu = SpbuUniversity.SpbuUniversity(programs)

        self.assertRaises(NotFound, spbu.get_position, "Name", "Surname", "Lastname")

    def test_get_position_should_throw_exception_when_student_is_not_exist(self):
        programs = programs_generator(3)

        spbu = SpbuUniversity.SpbuUniversity(programs)

        self.assertRaises(NotFound, spbu.get_position, "Notexistingname", "Notexistingsurname", "Notexistinglastname")

    def test_get_position_should_throw_exception_when_site_is_not_available(self):
        programs = programs_generator(5)
        programs.append(SpbuProgram("Bad request", "Bad request", "Bad request"))

        spbu = SpbuUniversity.SpbuUniversity(programs)

        self.assertRaises(BadRequest, spbu.get_position, "Name", "Surname", "Lastname")

    def test_get_position_should_works_correctly_when_programs_list_is_empty(self):
        programs = programs_generator(0)

        ranepa = SpbuUniversity.SpbuUniversity(programs)

        self.assertListEqual(ranepa.get_position("Name", "Surname", "Lastname"), list())

    def test_get_position_should_works_correctly_when_programs_list_contain_one_element(self):
        programs = programs_generator(1)

        ranepa = SpbuUniversity.SpbuUniversity(programs)

        result = [(SpbuProgram("EducationalForm0", "PayForm0", "Program0"), 10)]

        self.assertListEqual(ranepa.get_position("Name", "Surname", "Lastname"), result)

    def test_get_position_should_works_correctly_when_programs_list_contain_many_elements(self):
        programs = programs_generator(100)

        spbu = SpbuUniversity.SpbuUniversity(programs)

        result = list()
        for i in range(0, 100):
            result.append((programs[i], 10))

        self.assertListEqual(spbu.get_position("Name", "Surname", "Lastname"), result)

    def tearDown(self):
        SpbuUniversity.parser = spbu_parser


if __name__ == '__main__':
    unittest.main()
