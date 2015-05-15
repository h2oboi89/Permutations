import unittest

import sys, os, math

sys.path.insert(0, os.path.pardir)

import permute

class PermuteTestCase(unittest.TestCase):
    def test_perute(self):
        vals = []

        for i in range(5):
            vals.append(i)

            self.assertEqual(len(list(permute.permute(vals))), math.factorial(len(vals)))

if __name__ == '__main__':
    unittest.main()
