import unittest

from .challenge1 import challenge1
from .challenge2 import challenge2
from .challenge3 import challenge3

class SolutionMethods(unittest.TestCase):


    # test one
    def test_run(self):
        solution = challenge1()
        parameters = "hello"
        self.assertEqual(solution.run(parameters), "olleh")

    # test two
    def test_run2(self):
        solution = challenge2()
        parameters = 4
        self.assertEqual(solution.run(parameters), 8)

    # test three
    def test_run3(self):
        solution = challenge3()
        parameters = '{"name": "bob"}'
        self.assertEqual(solution.run(parameters), "bob")




if __name__ == "__main__":
    unittest.main()