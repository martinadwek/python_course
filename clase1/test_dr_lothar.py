import unittest

from clase1.dr_lothar import dr_lothar


class MyTestCase(unittest.TestCase):
    def test_even_number(self):
        self.assertEqual(8, dr_lothar(6))

    def test_odd_number(self):
        self.assertEqual(7, dr_lothar(3))

    def test_leq_zero_number(self):
        with self.assertRaises(ValueError):
            dr_lothar(-1)


if __name__ == '__main__':
    unittest.main()
