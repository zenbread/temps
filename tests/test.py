import unittest
import temperature


class TestTemp(unittest.TestCase):
    def test_create(self):
        self.assertIsNotNone(temperature.Temperature())

    def test_Cel(self):
        p = temperature.Temperature(C=1)
        self.assertIsNotNone(p.C)

    def test_Far(self):
        p = temperature.Temperature(F=1)
        self.assertEqual(p.F, 1)

    def test_Kel(self):
        p = temperature.Temperature(K=1)
        self.assertEqual(p.K, 1)

    def test_Del(self):
        p = temperature.Temperature(D=1)
        self.assertEqual(p.D, 1)

    def test_CelAll(self):
        p = temperature.Temperature(C=1)
        self.assertEqual(p.D, 148.5)
        self.assertEqual(p.K, 274.15)
        self.assertEqual(p.F, 33.8)
