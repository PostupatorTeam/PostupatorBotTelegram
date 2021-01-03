import unittest
from models.Program.implementations.SpbuProgram import SpbuProgram


class TestEtuProgram(unittest.TestCase):
    def setUp(self):
        self.program = SpbuProgram("ExampleEducationalForm", "ExamplePayForm", "ExampleProgram")

    def test_str_should_works_correctly_when_data_is_correct(self):
        result = "ExampleProgram/ExampleEducationalForm/ExamplePayForm"

        self.assertEqual(str(self.program), result)


if __name__ == '__main__':
    unittest.main()
