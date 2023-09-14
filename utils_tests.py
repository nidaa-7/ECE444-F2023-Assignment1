import unittest
from utils import Utils

class UtilsTests(unittest.TestCase):
    def testReversedWithInt(self):
        self.assertEqual(Utils.reversed(123456789), 987654321)
        self.assertEqual(Utils.reversed(-357), -753)
        self.assertEqual(Utils.reversed(3), 3)

    def testReversedWithStr(self):
        self.assertRaises(ValueError, Utils.reversed, "error")
        self.assertRaises(ValueError, Utils.reversed, "hey there")
        self.assertRaises(ValueError, Utils.reversed, "nidaa")

    def testReversedWithFloats(self):
        self.assertRaises(ValueError, Utils.reversed, 23.5)
        self.assertRaises(ValueError, Utils.reversed, 42.0)
        self.assertRaises(ValueError, Utils.reversed, 92.48)

    def testFormatterWithInt(self):
        self.assertEqual(Utils.formatter(7), ("0b111", "0o7"))
        self.assertEqual(Utils.formatter(16), ("0b10000", "0o20"))
        self.assertEqual(Utils.formatter(9248), ("0b10010000100000", "0o22040"))

    def testFormatterWithStr(self):
        self.assertRaises(ValueError, Utils.formatter, "error")
        self.assertRaises(ValueError, Utils.formatter, "hey there")
        self.assertRaises(ValueError, Utils.formatter, "nidaa")

    def testFormatterWithFloats(self):
        self.assertRaises(ValueError, Utils.formatter, 23.5)
        self.assertRaises(ValueError, Utils.formatter, 42.0)
        self.assertRaises(ValueError, Utils.formatter, 92.48)

if __name__ == '__main__':
    unittest.main()