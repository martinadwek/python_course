import unittest

from clase3.parenthesis import parenthesis_checker


class ParenthesisTestCase(unittest.TestCase):
    def test_no_closing_parenthesis(self):
        self.assertEqual(parenthesis_checker("((hthrf)[]"), False)
        self.assertEqual(parenthesis_checker("{{hthrf}[]"), False)
        self.assertEqual(parenthesis_checker("[[hthrf]{}"), False)

    def test_no_opening_parenthesis(self):
        self.assertEqual(parenthesis_checker(")(hthrf)[]"), False)
        self.assertEqual(parenthesis_checker("}{hthrf}[]"), False)
        self.assertEqual(parenthesis_checker("][hthrf]{}"), False)

    def test_empty_phrase(self):
        self.assertEqual(parenthesis_checker(""), True)
        
    def test_balanced_parenthesis(self):
        self.assertEqual(parenthesis_checker("(hthrf)[]"), True)
        self.assertEqual(parenthesis_checker("{hthrf}[]"), True)
        self.assertEqual(parenthesis_checker("[hthrf]{}"), True)
        
    def test_sandwiched_parenthesis(self):
        self.assertEqual(parenthesis_checker("([hthrf)][]"), False)
        self.assertEqual(parenthesis_checker("{(hthrf})[]"), False)
        self.assertEqual(parenthesis_checker("[{hthrf]}{}"), False)

    def test_inverted_parenthesis(self):
        self.assertEqual(parenthesis_checker(")("), False)
        self.assertEqual(parenthesis_checker("]["), False)
        self.assertEqual(parenthesis_checker("}{"), False)


if __name__ == '__main__':
    unittest.main()
