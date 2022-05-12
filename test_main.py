import unittest
from unittest import TestCase

from main import *


class MyTestCase(unittest.TestCase):
    def test_GPA(self):
        print(GPA([0, 0, 0, 0]))
        self.assertAlmostEqual(GPA([0, 0, 0, 0]), 0.0, delta=0.001)
        self.assertAlmostEqual(GPA([100, 100, 100, 100]), 4.0, delta=0.001)
        self.assertAlmostEqual(GPA([92, 92, 92, 92]), 3.7, delta=0.001)
        self.assertAlmostEqual(GPA([90, 90, 90, 90]), 3.7, delta=0.001)
        self.assertAlmostEqual(GPA([80, 80, 80, 80]), 2.7, delta=0.001)
        self.assertAlmostEqual(GPA([70, 70, 70, 70]), 1.7, delta=0.001)
        self.assertAlmostEqual(GPA([60, 60, 60, 60]), 0.7, delta=0.001)
        self.assertAlmostEqual(GPA([20, 83, 77, 64]), 1.575, delta=0.001)
        self.assertAlmostEqual(GPA([84, 84, 84, 84]), 3.0, delta=0.001)
        self.assertAlmostEqual(GPA([76, 76, 76, 76]), 2.0, delta=0.001)
        self.assertAlmostEqual(GPA([64, 65, 66, 66]), 1.0, delta=0.001)
        self.assertAlmostEqual(GPA([55, 33, 22, 22]), 0.0, delta=0.001)
        self.assertAlmostEqual(GPA([100, 0, 1, 43]), 1.0, delta=0.001)





if __name__ == '__main__':
    unittest.main()



