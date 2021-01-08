import unittest
from src.main.models.Program.implementations.EtuProgram import EtuProgram


class TestEtuProgram(unittest.TestCase):
    def setUp(self):
        self.program = EtuProgram("ExampleForm", "ExampleProgram")

    def test_str_should_works_correctly_when_data_is_correct(self):
        result = "ExampleForm/ExampleProgram"

        self.assertEqual(str(self.program), result)


if __name__ == '__main__':
    unittest.main()
