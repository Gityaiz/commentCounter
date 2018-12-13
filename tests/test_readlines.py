import unittest
import sys
import os
sys.path.append(r'..\module')
sys.path.append(r'..\testDir')
import readlines as rl

'''
# readlines ⇒ classify_C_enable_or_comment の呼び出し依存関係があるため
# classify_C_enable_or_comment が正しいことを前提とする
'''


class Testreadlines(unittest.TestCase):
    def test_readlines1(self):
        filename = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.dirname(filename) + r'\testDir\15_8_11.c'
        expect = {'allLine': 15, 'enableLine': 8, 'commentLine': 11}
        actual = rl.readlines(filename)
        self.assertEqual(expect, actual)


if __name__ == "__main__":
    unittest.main()
