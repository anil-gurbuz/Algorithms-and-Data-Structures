import unittest
import calculator


class test_for_calculatoy(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(calculator.sum(3,5),8)

    def test_sub(self):
        self.assertTrue(calculator.sub(5,4)==1)

    def test_mult(self):
        self.assertEqual(calculator.mult(2,3),6)

    def test_div(self):
        self.assertEqual(calculator.div(5,2),2)

