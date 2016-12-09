import unittest
from format_price import format_price

class TestFormattingPrice(unittest.TestCase):

    def test_normal_int(self):
        formatted_price = format_price(3445)
        self.assertEqual(formatted_price, '3 445')

    def test_int_with_decimal_point(self):
        formatted_price = format_price(3445.000000)
        self.assertEqual(formatted_price, '3 445')

    def test_normal_float(self):
        formatted_price = format_price(3445.543346)
        self.assertEqual(formatted_price, '3 445.54')

    def test_incorrect_input(self):
        formatted_price = format_price('3445d')
        self.assertEqual(formatted_price, None)

    def test_negative_number(self):
        formatted_price = format_price(-312)
        self.assertEqual(formatted_price, None)


if __name__ == '__main__':
    unittest.main()
