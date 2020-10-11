import unittest

from clase2.alphabet import translate


class AlphabetTestCase(unittest.TestCase):
    def test_no_special_chars(self):
        self.assertEqual(translate("𐌀𐌋𐌅𐌀𐌁𐌄𐌕𐌏"), "ALFABETO")

    def test_special_chars(self):
        self.assertEqual(translate("¿𐌔𐌉 𐌏 𐌍𐌏? 𐌌𐌌𐌌... 𐌔𐌉."), "¿SI O NO? MMM... SI.")

    def test_empty_string(self):
        self.assertEqual(translate(""), "")


if __name__ == '__main__':
    unittest.main()
