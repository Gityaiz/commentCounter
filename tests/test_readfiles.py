import unittest
import sys
sys.path.append('../module')
import readfiles as rf

class Test_readfiles(unittest.TestCase):
    def test_readfiles(self):
        expect = [{'allLine': 15, 'enableLine': 8, 'commentLine': 11, 'filename': "../testDir\\15_8_11.c"},\
                  {'allLine': 7, 'enableLine': 4, 'commentLine': 3, 'filename': "../testDir\\2\\7_4_3.h"}]
        actual = rf.readfiles("../testDir", 1)
        self.assertEqual(expect, actual)


if __name__ == "__main__":
    unittest.main()
