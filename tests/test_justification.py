import unittest
import sys

sys.path.append('../module')
import Justification as ju


class test_justification(unittest.TestCase):

    def test_left1(self):
        expect = "test      "
        actual = ju.left(10, 'test')
        self.assertEqual(expect, actual)

    def test_left2(self):
        expect = "テスト    "
        actual = ju.left(10, 'テスト')
        self.assertEqual(expect, actual)

    def test_left3(self):
        expect = "tesと     "
        actual = ju.left(10, 'tesと')
        self.assertEqual(expect, actual)

    def test_left4(self):
        expect = "てst      "
        actual = ju.left(10, 'てst      ')
        self.assertEqual(expect, actual)

    def test_right1(self):
        expect = "      test"
        actual = ju.right(10, 'test')
        self.assertEqual(expect, actual)

    def test_right2(self):
        expect = "    テスト"
        actual = ju.right(10, 'テスト')
        self.assertEqual(expect, actual)

    def test_right3(self):
        expect = "     tesと"
        actual = ju.right(10, 'tesと')
        self.assertEqual(expect, actual)

    def test_right4(self):
        expect = "      てst"
        actual = ju.right(10, 'てst')
        self.assertEqual(expect, actual)


if __name__ == "__main__":
    unittest.main()
