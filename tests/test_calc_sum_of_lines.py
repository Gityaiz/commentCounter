import unittest
import sys
sys.path.append('../module')

import calc_sum_of_lines as sol

class Test_calc_sum_of_lines(unittest.TestCase):
    def test_calc_sum_of_lines1(self):
        directory1 = {'allLine': 5, 'enableLine': 2, 'commentLine': 3}
        directory2 = {'allLine': 5, 'enableLine': 2, 'commentLine': 3}

        list = [directory1, directory2]
        expect = (10, 4, 6)
        actual = sol.calc_sum_of_lines(list)
        self.assertEqual(expect, actual)


if __name__ == "__main__":
    unittest.main()

