import unittest

from .challenge1 import challenge1
from .challenge2 import challenge2
from .challenge3 import challenge3


class SolutionMethods(unittest.TestCase):

    # test one
    def test_run(self):
        solution = challenge1()
        parameters = '{"name":"Billy", "age":25, "city":"London", "job":"being awesome"}'
        self.assertEqual(solution.run(parameters), "being awesome")

    # test two
    def test_run2(self):
        solution = challenge2()
        parameters = {
            "blue": 10,
            "red": 5,
            "yellow": 2
        }
        self.assertEqual(solution.run(parameters), '{"blue":10, "red":5, "yellow": 2}')

    # test three
    def test_run3(self):
        solution = challenge3()
        parameters = '[{"name":"Billy", "age":25, "city":"London", "job":"being awesome"},' \
                     '{ "name":"TOM", "age":22, "city":"London", "job":"being awesome"},' \
                     '{ "name":"DOGO", "age":"24", "city":"BBOP", "job":"being being"}]'
        self.assertEqual(solution.run(parameters), ["Billy", "TOM", "DOGO"])


if __name__ == "__main__":
    unittest.main()
