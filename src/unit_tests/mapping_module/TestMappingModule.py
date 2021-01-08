from werkzeug.exceptions import NotFound, BadRequest
from src.main.mapping_module.mapping_module import map_to_concrete_university_students, map_to_student
from src.main.models.ConcreteUniversityStudent.implementations.EtuStudent import EtuStudent
from src.main.models.ConcreteUniversityStudent.implementations.RanepaStudent import RanepaStudent
from src.main.models.ConcreteUniversityStudent.implementations.SpbuStudent import SpbuStudent
from src.main.models.Program.implementations.EtuProgram import EtuProgram
from src.main.models.Program.implementations.SpbuProgram import SpbuProgram
from src.main.models.Student import Student
from src.main.models.University.implementations import RanepaUniversity, SpbuUniversity, EtuUniversity
import unittest
from src.main.parsing_module.parsers import ranepa_parser, etu_parser, spbu_parser
from src.unit_tests.mapping_module.parsers import etu_test_parser, ranepa_test_parser, spbu_test_parser


class TestMappingModule(unittest.TestCase):
    def setUp(self):
        SpbuUniversity.parser = spbu_test_parser
        EtuUniversity.parser = etu_test_parser
        RanepaUniversity.parser = ranepa_test_parser

    def test_map_to_concrete_university_students_should_throw_BadRequest_when_university_throws_BadRequest(self):
        universities = [SpbuUniversity.SpbuUniversity([SpbuProgram("Bad request", "Bad request", "Bad request")])]
        student = Student("Userid", "Name", "Surname", "Lastname", universities)

        self.assertRaises(BadRequest, map_to_concrete_university_students, student)

    def test_map_to_concrete_university_students_should_throw_NotFound_when_university_throws_NotFound(self):
        universities = [SpbuUniversity.SpbuUniversity([SpbuProgram("Example", "Example", "Example")])]
        student = Student("Userid", "Notexistingname", "Notexistingsurname", "Notexistinglastname", universities)

        self.assertRaises(NotFound, map_to_concrete_university_students, student)

    def test_map_to_concrete_university_students_should_work_correctly_when_university_list_is_empty(self):
        universities = list()
        student = Student("Userid", "Name", "Surname", "Lastname", universities)

        self.assertListEqual(map_to_concrete_university_students(student), list())

    def test_map_to_concrete_university_students_should_work_correctly_when_university_list_is_not_empty(self):
        spbu_programs = [SpbuProgram("Form0", "Form0", "Program0")]
        etu_programs = [EtuProgram("Form0", "Program0"), EtuProgram("Form1", "Program1")]
        ranepa_programs = list()

        universities = [SpbuUniversity.SpbuUniversity(spbu_programs),
                        EtuUniversity.EtuUniversity(etu_programs),
                        RanepaUniversity.RanepaUniversity(ranepa_programs)]

        student = Student("Userid", "Name", "Surname", "Lastname", universities)

        result = [SpbuStudent("Userid", "Name", "Surname", "Lastname", [(spbu_programs[0], 10)]),
                  EtuStudent("Userid", "Name", "Surname", "Lastname", [(etu_programs[0], 10), (etu_programs[1], 10)]),
                  RanepaStudent("Userid", "Name", "Surname", "Lastname", [])]

        self.assertListEqual(map_to_concrete_university_students(student), result)

    def test_map_to_student_should_work_correctly(self):
        spbu_programs = [SpbuProgram("Form0", "Form0", "Program0")]
        etu_programs = [EtuProgram("Form0", "Program0"), EtuProgram("Form1", "Program1")]
        ranepa_programs = list()

        students = [SpbuStudent("Userid", "Name", "Surname", "Lastname", [(spbu_programs[0], 10)]),
                    EtuStudent("Userid", "Name", "Surname", "Lastname", [(etu_programs[0], 10), (etu_programs[1], 10)]),
                    RanepaStudent("Userid", "Name", "Surname", "Lastname", [])]

        universities = [SpbuUniversity.SpbuUniversity(spbu_programs),
                        EtuUniversity.EtuUniversity(etu_programs),
                        RanepaUniversity.RanepaUniversity(ranepa_programs)]

        result = map_to_student(students)

        self.assertEqual(result.userid, "Userid")
        self.assertEqual(result.name, "Name")
        self.assertEqual(result.surname, "Surname")
        self.assertEqual(result.lastname, "Lastname")
        for i in range(0, len(universities)):
            self.assertListEqual(result.universities[i].programs, universities[i].programs)

    def tearDown(self):
        SpbuUniversity.parser = spbu_parser
        EtuUniversity.parser = etu_parser
        RanepaUniversity.parser = ranepa_parser


if __name__ == '__main__':
    unittest.main()
