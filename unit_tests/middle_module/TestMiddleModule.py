from psycopg2._psycopg import InternalError
from werkzeug.exceptions import NotFound, BadRequest
from database_module import database_module
from middle_module import middle_module
from models.Program.implementations.EtuProgram import EtuProgram
from models.Program.implementations.RanepaProgram import RanepaProgram
from models.Program.implementations.SpbuProgram import SpbuProgram
from models.Student import Student
from models.University.implementations import SpbuUniversity, EtuUniversity, RanepaUniversity
import unittest
from parsing_module.parsers import spbu_parser, etu_parser, ranepa_parser
from unit_tests.middle_module.parsers import spbu_test_parser, etu_test_parser, ranepa_test_parser
from unit_tests.middle_module.database import test_database_module


class TestMiddleModule(unittest.TestCase):
    def setUp(self):
        SpbuUniversity.parser = spbu_test_parser
        EtuUniversity.parser = etu_test_parser
        RanepaUniversity.parser = ranepa_test_parser
        middle_module.database_module = test_database_module

    def test_send_notifications_should_work_correctly_when_database_module_return_empty_list(self):
        test_database_module.quantity_with_notifications = 0

        self.assertDictEqual(middle_module.send_notifications(), dict())

    def test_send_notifications_should_work_correctly_when_database_module_return_not_empty_list(self):
        test_database_module.quantity_with_notifications = 3

        result = {"userid0": {"СПБГУ": [(SpbuProgram("Example0", "Example0", "Example0"), 3)],
                              "ЛЭТИ": [(EtuProgram("Example0", "Example0"), 5)],
                              "РАНХИГС": [(RanepaProgram("Example0", "Example0", "Example0", "Example0"), 10)]},
                  "userid1": {"СПБГУ": [(SpbuProgram("Example0", "Example0", "Example0"), 3),
                                        (SpbuProgram("Example1", "Example1", "Example1"), 3)]},
                  "userid2": {"СПБГУ": [(SpbuProgram("Example0", "Example0", "Example0"), 3),
                                        (SpbuProgram("Example1", "Example1", "Example1"), 3),
                                        (SpbuProgram("Example2", "Example2", "Example2"), 3)],
                              "ЛЭТИ": [(EtuProgram("Example0", "Example0"), 5),
                                       (EtuProgram("Example1", "Example1"), 5),
                                       (EtuProgram("Example2", "Example2"), 5)]}}

        self.assertDictEqual(middle_module.send_notifications(), result)

    def test_create_user_should_throw_NotFound_when_university_throw_NotFound(self):
        universities = [SpbuUniversity.SpbuUniversity([SpbuProgram("Example", "Example", "Example")])]
        student = Student("Userid", "Notexistingname", "Notexistingsurname", "Notexistinglastname", universities)

        self.assertRaises(NotFound, middle_module.create_user, student)

    def test_create_user_should_throw_BadRequest_when_university_throw_BadRequest(self):
        universities = [EtuUniversity.EtuUniversity([EtuProgram("Bad request", "Bad request")])]
        student = Student("Userid", "Name", "Surname", "Lastname", universities)

        self.assertRaises(BadRequest, middle_module.create_user, student)

    def test_create_user_should_throw_InternalError_when_database_module_return_false(self):
        universities = [EtuUniversity.EtuUniversity([EtuProgram("Example", "Example")])]
        student = Student("ExistingId", "Name", "Surname", "Lastname", universities)

        self.assertRaises(InternalError, middle_module.create_user, student)

    def test_create_user_should_work_correctly_when_data_is_correct(self):
        spbu = SpbuUniversity.SpbuUniversity([SpbuProgram("Form", "Form", "Program")])
        ranepa = RanepaUniversity.RanepaUniversity([RanepaProgram("Departament", "Approval", "Form", "Program")])
        etu = EtuUniversity.EtuUniversity([EtuProgram("Form0", "Program0"), EtuProgram("Form1", "Program1")])
        universities = [spbu, ranepa, etu]

        student = Student("UserId", "Name", "Surname", "Lastname", universities)

        result = {"СПБГУ": [(SpbuProgram("Form", "Form", "Program"), 3)],
                  "РАНХИГС": [(RanepaProgram("Departament", "Approval", "Form", "Program"), 10)],
                  "ЛЭТИ": [(EtuProgram("Form0", "Program0"), 5), (EtuProgram("Form1", "Program1"), 5)]}

        self.assertDictEqual(middle_module.create_user(student), result)

    def test_edit_user_should_throw_NotFound_when_university_throw_NotFound(self):
        universities = [SpbuUniversity.SpbuUniversity([SpbuProgram("Example", "Example", "Example")])]
        student = Student("Userid", "Notexistingname", "Notexistingsurname", "Notexistinglastname", universities)

        self.assertRaises(NotFound, middle_module.edit_user, student)

    def test_edit_user_should_throw_BadRequest_when_university_throw_BadRequest(self):
        universities = [EtuUniversity.EtuUniversity([EtuProgram("Bad request", "Bad request")])]
        student = Student("Userid", "Name", "Surname", "Lastname", universities)

        self.assertRaises(BadRequest, middle_module.edit_user, student)

    def test_edit_user_should_throw_InternalError_when_database_module_return_false(self):
        universities = [EtuUniversity.EtuUniversity([EtuProgram("Example", "Example")])]
        student = Student("NotExistingId", "Name", "Surname", "Lastname", universities)

        self.assertRaises(InternalError, middle_module.edit_user, student)

    def test_edit_user_should_work_correctly_when_data_is_correct(self):
        spbu = SpbuUniversity.SpbuUniversity([SpbuProgram("Form", "Form", "Program")])
        etu = EtuUniversity.EtuUniversity([EtuProgram("Form0", "Program0"), EtuProgram("Form1", "Program1")])
        universities = [spbu, etu]

        student = Student("UserId", "Name", "Surname", "Lastname", universities)

        result = {"СПБГУ": [(SpbuProgram("Form", "Form", "Program"), 3)],
                  "ЛЭТИ": [(EtuProgram("Form0", "Program0"), 5), (EtuProgram("Form1", "Program1"), 5)]}

        self.assertDictEqual(middle_module.edit_user(student), result)

    def test_get_info_should_throw_NotFound_when_university_throw_NotFound(self):
        userid = "StudentWithNotExistingData"

        self.assertRaises(NotFound, middle_module.get_info, userid)

    def test_get_info_should_throw_BadRequest_when_university_throw_BadRequest(self):
        userid = "badrequest"

        self.assertRaises(BadRequest, middle_module.get_info, userid)

    def test_get_info_should_throw_InternalError_when_database_module_throw_InternalError(self):
        userid = "NotExistingId"

        self.assertRaises(InternalError, middle_module.get_info, userid)

    def test_get_info_should_work_correctly_when_data_is_correct(self):
        result = {"СПБГУ": [(SpbuProgram("Example0", "Example0", "Example0"), 3)],
                  "ЛЭТИ": [(EtuProgram("Example0", "Example0"), 5), (EtuProgram("Example1", "Example1"), 5)],
                  "РАНХИГС": [(RanepaProgram("Example0", "Example0", "Example0", "Example0"), 10),
                              (RanepaProgram("Example1", "Example1", "Example1", "Example1"), 10),
                              (RanepaProgram("Example2", "Example2", "Example2", "Example2"), 10)]}

        self.assertDictEqual(middle_module.get_info("UserId"), result)

    def test_add_notifications_should_throw_InternalError_when_database_module_throw_InternalError(self):
        self.assertRaises(InternalError, middle_module.add_notifications, "NotExistingId")

    def test_add_notifications_should_return_false_when_database_module_return_false(self):
        self.assertFalse(middle_module.add_notifications("UserIdWithNotifications"))

    def test_add_notifications_should_return_true_when_database_module_return_true(self):
        self.assertTrue(middle_module.add_notifications("UserIdWithoutNotifications"))

    def test_remove_notifications_should_throw_InternalError_when_database_module_throw_InternalError(self):
        self.assertRaises(InternalError, middle_module.remove_notifications, "NotExistingId")

    def test_remove_notifications_should_return_false_when_database_module_return_false(self):
        self.assertFalse(middle_module.remove_notifications("UserIdWithoutNotifications"))

    def test_remove_notifications_should_return_true_when_database_module_return_true(self):
        self.assertTrue(middle_module.remove_notifications("UserIdWithNotifications"))

    def tearDown(self):
        SpbuUniversity.parser = spbu_parser
        EtuUniversity.parser = etu_parser
        RanepaUniversity.parser = ranepa_parser
        middle_module.database_module = database_module


if __name__ == '__main__':
    unittest.main()
