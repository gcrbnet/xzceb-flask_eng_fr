import unittest

from translator import englishtofrench, frenchtoenglish


class testenglishtofrench(unittest.TestCase):
    def test_englishtofrench(self):
        self.assertEqual(englishtofrench("Hello"),"Bonjour")
        self.assertNotEqual(englishtofrench("Hello"),"Hello")

class testfrenchtoenglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchtoenglish("Bonjour"),"Hello")
        self.assertNotEqual(frenchtoenglish("Bonjour"),"Bonjour")

unittest.main()