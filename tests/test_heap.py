import unittest

import sys, os, math

sys.path.insert(0, os.path.pardir)

import heap

class HeapTestCase(unittest.TestCase):
    def test_heap(self):
        vals = []

        for i in range(5):
            vals.append(i)

            self.assertEqual(len(list(heap.generate(vals))), math.factorial(len(vals)))

if __name__ == '__main__':
    unittest.main()
