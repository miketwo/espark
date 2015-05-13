#!/usr/bin/env python
import unittest

from espark import Level, levels_from_string
from espark import Student


class StudentTests(unittest.TestCase):
    def test_init_nominal(self):
        # None should throw
        Student('Alice', levels_from_string('K.RL,2.RI'))
        Student('Bob', levels_from_string('0.RL,None.RI'))
        Student('Charles', levels_from_string('K.RL,5.RI,None.BL'))
        Student('Derek', 'AA')
        Student('Emily', 'AA')
        Student('Fred', 'AA')


class PathCreationTests(unittest.TestCase):
    def setUp(self):
        # For all of these tests, we'll use the same basic level ordering
        self.order = levels_from_string(
            "K.AA,K.BB,"
            "1.AA,1.BB,"
            "2.BB,2.AA,"  # Change the order of topics
            "3.BB,3.AA,3.CC,"  # Introduce a new domain
            "4.AA,4.CC")  # Remove a domain

    def test_blank_student(self):
        # A student with no test results at all
        # Also tests that results are limited to 5
        expected = levels_from_string("[K.AA, K.BB, 1.AA, 1.BB, 2.BB]")
        result = Student('Alice', []).path(self.order)
        self.assertSequenceEqual(expected, result)

    def test_max_student(self):
        # This is a student who has mastered everything
        expected = []
        alice = Student('Alice', levels_from_string("5.AA,4.BB,5.CC"))
        result = alice.path(self.order)
        self.assertSequenceEqual(expected, result)

    def test_less_than_5_results(self):
        expected = [Level(4, "AA")]
        alice = Student('Alice', levels_from_string("4.AA,4.BB,5.CC"))
        result = alice.path(self.order)
        self.assertSequenceEqual(expected, result)

    def test_correct_changing_order_of_domains(self):
        # Notice that 1st grade is AA --> BB, whereas 2nd grade is opposite
        expected = levels_from_string("[1.AA, 1.BB, 2.BB, 2.AA, 3.BB]")
        alice = Student('Alice', levels_from_string("1.AA,1.BB,5.CC"))
        result = alice.path(self.order)
        self.assertSequenceEqual(expected, result)


class LevelTests(unittest.TestCase):
    def test_init(self):
        # Nominal (none of these should throw)
        Level("K", "AA")
        Level(0, "AA")
        Level(5, "AA")
        Level(None, "AA")
        Level("", "AA")  # Same as None

    def test_levels_from_string(self):
        expected = [Level('K', "AA")]
        result = levels_from_string('K.AA')
        self.assertEqual(expected, result)

        expected = [Level('K', "AA"), Level('1', "BB")]
        result = levels_from_string('K.AA,1.BB')
        self.assertEqual(expected, result)

        expected = [Level('K', "AA"), Level('1', "BB")]
        result = levels_from_string('[K.AA, 1.BB]')
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
