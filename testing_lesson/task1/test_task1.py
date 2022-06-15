import unittest
from task1 import skaiciu_suma, saraso_suma, didziausias_skaicius, stringas_atbulai, info_apie_sakini

class TestKeliamieji3(unittest.TestCase):
    def test_skaiciu_suma(self):
        self.assertEqual(6, skaiciu_suma(1, 2, 3))
        self.assertEqual(3, skaiciu_suma(1, 1, 1))
        self.assertEqual(4, skaiciu_suma(1, 1, 2))

    def test_saraso_suma(self):
        self.assertEqual(6, saraso_suma([1, 2, 3]))
        self.assertEqual(3, saraso_suma([1, 1, 1]))
        self.assertEqual(5, saraso_suma([1, 1, 2, 1]))

    def test_didziausias_skaicius(self):
        self.assertEqual(55, didziausias_skaicius(1, 55, 3))
        self.assertEqual(101, didziausias_skaicius(1, 101, 1))
        self.assertEqual(88, didziausias_skaicius(1, 88, 2, 1))

    def test_stringas_atbulai(self):
        self.assertEqual("olleH", stringas_atbulai("Hello"))
        self.assertEqual("sdrac", stringas_atbulai("cards"))
        self.assertEqual("nohtyP", stringas_atbulai("Python"))
    
    def test_info_apie_sakini(self):
        self.assertEqual({"didziosios": 1, "mazolio": 4, "skaiciai": 0}, info_apie_sakini("Hello"))
        self.assertEqual({"didziosios": 1, "mazolio": 4, "skaiciai": 3}, info_apie_sakini("Hello 123"))
        self.assertEqual({"didziosios": 2, "mazolio": 3, "skaiciai": 3}, info_apie_sakini("HellO 123"))
        
   
if __name__ == '__main__':
    unittest.main()