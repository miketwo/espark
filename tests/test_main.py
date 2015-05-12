#!/usr/bin/env python
import unittest
import sys
import os
sys.path.append("..")

import time

import difflib
def show_diff(seqm):
    """Unify operations between two compared strings
seqm is a difflib.SequenceMatcher instance whose a & b are strings"""
    output= []
    for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
        if opcode == 'equal':
            output.append(seqm.a[a0:a1])
        elif opcode == 'insert':
            output.append("<ins>" + seqm.b[b0:b1] + "</ins>")
        elif opcode == 'delete':
            output.append("<del>" + seqm.a[a0:a1] + "</del>")
        elif opcode == 'replace':
            output.append("<r>" + seqm.a[a0:a1] + '/' + seqm.b[b0:b1] + "</r>")
        else:
            raise RuntimeError, "unexpected opcode"
    return ''.join(output)

from espark import main as espark


LOCATION = os.path.dirname(os.path.realpath(__file__))
ALL_LEVELS = espark.create_ordering_from_csv(
            os.path.join(LOCATION, "../data/domain_order.csv"))

class EsparkTests(unittest.TestCase):

    def test_create_student_from_csv(self):
        students = espark.create_students_from_csv(
            os.path.join(LOCATION, "../data/student_tests.csv"))
        # for s in students:
        #     print s

    def test_create_ordering_from_csv(self):
        levels = espark.create_ordering_from_csv(
            os.path.join(LOCATION, "../data/domain_order.csv"))
        # for l in levels:
        #     print l

    def test_efficiency(self):
        start = time.time()
        for i in range(1000):
            espark.creates_paths(
                os.path.join(LOCATION, "../data/student_tests.csv"),
                os.path.join(LOCATION, "../data/domain_order.csv"))
        end = time.time()
        print end-start

    def test_fast_filter(self):
        levels = espark.make_levels("K.RF,K.RL,K.RI,1.RF,1.RL,1.RI,2.RF,2.RI,2.RL,2.L,3.RF,3.RL,3.RI,3.L,4.RI,4.RL,4.L,5.RI,5.RL,5.L,6.RI,6.RL")
        expected = espark.make_levels("2.L,3.RF,3.L,4.RI,4.L,5.RI,5.RL,5.L,6.RI,6.RL")
        student_levels = espark.make_levels("3.RF,4.RI,5.RL")
        result = espark.fast_filter(student_levels, levels)
        self.assertSequenceEqual(expected, result)

    def test_lower_levels(self):
        expected = [espark.Level("K", "AA"),
                    espark.Level(1, "AA"),
                    espark.Level(2, "AA"),
                    espark.Level(3, "AA"),
                    espark.Level(4, "AA")]
        result = espark.Level(5, "AA").lower_levels()
        self.assertSequenceEqual(expected, result)

    def test_lower_levels_edgecase_low(self):
        expected = []
        result = espark.Level("K", "AA").lower_levels()
        self.assertSequenceEqual(expected, result)

    def test_equality_different_domain(self):
        self.assertFalse(espark.Level("K", "AA") == espark.Level("K", "BB"))
        self.assertFalse(espark.Level(1, "AA") == espark.Level(1, "BB"))

    def test_equality_same_domain(self):
        self.assertTrue(espark.Level("K", "AA") == espark.Level("K", "AA"))
        self.assertTrue(espark.Level(1, "AA") == espark.Level(1, "AA"))
        self.assertTrue(espark.Level("K", "AA") == espark.Level(0, "AA"))

    def test_solution(self):
        students = espark.create_students_from_csv(
            os.path.join(LOCATION, "../data/student_tests.csv"))
        levels = espark.create_ordering_from_csv(
            os.path.join(LOCATION, "../data/domain_order.csv"))
        result = []
        for student in students:
            path = espark.calculate_path(student, levels)
            pathstr = ",".join(str(p) for p in path)
            result.append("{},{}".format(student.name, pathstr))
        with open(os.path.join(LOCATION, "../data/sample_solution.csv")) as f:
            print
            for idx, line in enumerate(f):
                # print "TRY :" + result[idx]
                # print "SOLN:" + line.strip()
                a = result[idx]
                b = line.strip()
                self.assertEqual(a, b)

    def test_membership(self):
        levels = [espark.Level("K", "AA"),
                  espark.Level(2, "AA"),
                  espark.Level(3, "AA"),
                  espark.Level(4, "AA"),
                  espark.Level(5, "AA")]
        self.assertTrue(espark.Level(3, "AA") in levels)
        self.assertTrue(espark.Level("K", "AA") in levels)
        self.assertFalse(espark.Level(1, "AA") in levels)
        self.assertTrue(espark.Level(3, "AA") in set(levels))
        self.assertTrue(espark.Level("K", "AA") in set(levels))
        self.assertFalse(espark.Level(1, "AA") in set(levels))

    def test_no_scores_starts_at_beginning(self):
        # tbd
        pass

if __name__ == '__main__':
    unittest.main()
