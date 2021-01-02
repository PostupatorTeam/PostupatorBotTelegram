import unittest
from models.Program.implementations.RanepaProgram import RanepaProgram


class TestEtuProgram(unittest.TestCase):
    def setUp(self):
        self.program = RanepaProgram("ExampleDepartament", "ExampleApproval", "ExampleForm", "ExampleProgram")

    def test_str_should_works_correctly_when_data_is_correct(self):
        result = "ExampleDepartament/ExampleApproval/ExampleForm/ExampleProgram"

        self.assertEqual(str(self.program), result)


if __name__ == '__main__':
    unittest.main()
