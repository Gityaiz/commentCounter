import unittest
import sys
sys.path.append('../module')
import count_enablecommentline as ce

ENABLE = 0
COMMENT = 1


class TestanalizeStatement(unittest.TestCase):

    def test_analizeStatement1(self):
        statement = ENABLE
        AnalizedLine_is = r"//test"
        expect = {'allLine': 1, 'enableLine': 0, 'commentLine': 1, 'currentStatus': ENABLE}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement2(self):
        statement = ENABLE
        AnalizedLine_is = r"/*comment*///comment"
        expect = {'allLine': 1, 'enableLine': 0, 'commentLine': 1, 'currentStatus': ENABLE}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement3(self):
        statement = ENABLE
        AnalizedLine_is = r"/* comment */ enabletext //comment"
        expect = {'allLine': 1, 'enableLine': 1, 'commentLine': 1, 'currentStatus': ENABLE}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement4(self):
        statement = ENABLE
        AnalizedLine_is = r"/* comment */"
        expect = {'allLine': 1, 'enableLine': 0, 'commentLine': 1, 'currentStatus': ENABLE}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)
    
    def test_analizeStatement5(self):
        statement = ENABLE
        AnalizedLine_is = r"/* comment */ enabletext"
        expect = {'allLine': 1, 'enableLine': 1, 'commentLine': 1, 'currentStatus': ENABLE}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement6(self):
        statement = ENABLE
        AnalizedLine_is = r"/* comment"
        expect = {'allLine': 1, 'enableLine': 0, 'commentLine': 1, 'currentStatus': COMMENT}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement7(self):
        statement = ENABLE
        AnalizedLine_is = r"enabletext /* comment*/"
        expect = {'allLine': 1, 'enableLine': 1, 'commentLine': 1, 'currentStatus': ENABLE}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement8(self):
        statement = ENABLE
        AnalizedLine_is = r"enabletext /* comment"
        expect = {'allLine': 1, 'enableLine': 1, 'commentLine': 1, 'currentStatus': COMMENT}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement9(self):
        statement = ENABLE
        AnalizedLine_is = r"enabletext // comment"
        expect = {'allLine': 1, 'enableLine': 1, 'commentLine': 1, 'currentStatus': ENABLE}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    # ここからコメント行中(statement = COMMENT)のパターン
    def test_analizeStatement11(self):
        statement = COMMENT
        AnalizedLine_is = r"//test"
        expect = {'allLine': 1, 'enableLine': 0, 'commentLine': 1, 'currentStatus': COMMENT}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement12(self):
        statement = COMMENT
        AnalizedLine_is = r"/*comment*///comment"
        expect = {'allLine': 1, 'enableLine': 0, 'commentLine': 1, 'currentStatus': ENABLE}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement13(self):
        statement = COMMENT
        AnalizedLine_is = r"/* comment */ enabletext //comment"
        expect = {'allLine': 1, 'enableLine': 1, 'commentLine': 1, 'currentStatus': ENABLE}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement14(self):
        statement = COMMENT
        AnalizedLine_is = r"/* comment */"
        expect = {'allLine': 1, 'enableLine': 0, 'commentLine': 1, 'currentStatus': ENABLE}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)
    
    def test_analizeStatement15(self):
        statement = COMMENT
        AnalizedLine_is = r"/* comment */ enabletext"
        expect = {'allLine': 1, 'enableLine': 1, 'commentLine': 1, 'currentStatus': ENABLE}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement16(self):
        statement = COMMENT
        AnalizedLine_is = r"/* comment"
        expect = {'allLine': 1, 'enableLine': 0, 'commentLine': 1, 'currentStatus': COMMENT}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement17(self):
        statement = COMMENT
        AnalizedLine_is = r"enabletext /* comment*/"
        expect= {'allLine': 1, 'enableLine': 0, 'commentLine': 1, 'currentStatus': ENABLE}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement18(self):
        statement = COMMENT
        AnalizedLine_is = r"enabletext /* comment"
        expect = {'allLine': 1, 'enableLine': 0, 'commentLine': 1, 'currentStatus': COMMENT}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement19(self):
        statement = COMMENT
        AnalizedLine_is = r"enabletext // comment"
        expect = {'allLine': 1, 'enableLine': 0, 'commentLine': 1, 'currentStatus': COMMENT}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement20(self):
        statement = COMMENT
        AnalizedLine_is = r"enabletext // comment"
        expect = {'allLine': 1, 'enableLine': 0, 'commentLine': 1, 'currentStatus': COMMENT}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement21(self):
        statement = ENABLE
        AnalizedLine_is = r"#include <stdio.h>"
        expect = {'allLine': 1, 'enableLine': 1, 'commentLine': 0, 'currentStatus': ENABLE}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)

    def test_analizeStatement22(self):
        statement = ENABLE
        AnalizedLine_is = ""
        expect = {'allLine': 1, 'enableLine': 0, 'commentLine': 0, 'currentStatus': ENABLE}
        actual = ce.classify_C_enable_or_comment(statement, AnalizedLine_is)
        self.assertEqual(expect, actual)


if __name__ == "__main__":
    unittest.main()
