import unittest
from keliamieji import *

# class TestKeliamieji(unittest.TestCase):

#     def test_ar_keliamieji(self):
#         rezultatas = ar_keliamieji(2000)
#         lukestis = "Keliamieji"
#         self.assertEqual(lukestis, rezultatas)


#     def test_ar_keliamieji1(self):
#         rezultatas = ar_keliamieji(2010)
#         lukestis = "Keliamieji"
#         self.assertEqual(lukestis, rezultatas)

class TestKeliamieji(unittest.TestCase):
    def test_ar_keliamieji(self):
        self.assertEqual("Keliamieji", ar_keliamieji(2000))
        self.assertEqual("Keliamieji", ar_keliamieji(2020))
        self.assertEqual("Nekeliamieji", ar_keliamieji(2100))

if __name__ == '__main__':
    unittest.main()