"""
Greatest common divisor.
"""


def gcd_div(num1, num2):
    """
    Takes two non-negative integers and returns greatest
    common divisor of these numbers.

    Implementation of Euclidean algorithm:
    gcd(a, 0) = a
    gcd(a, b) = gcd(b, a mod b)
    """
    if num1 * num2 == 0:
        return num1 + num2

    return gcd_div(num2, num1 % num2)


def gcd_sub(num1, num2):
    """
    Takes two non-negative integers and returns greatest
    common divisor of these numbers.

    Implementation of Euclidean algorithm:
    gcd(a, a) = a
    gcd(a, b) = gcd(a - b, b)   if a > b
    gcd(a, b) = gcd(a, b - a)   if b > a
    """
    if num1 * num2 == 0:
        return num1 + num2

    if num1 > num2:
        return gcd_sub(num1 - num2, num2)
    else:
        return gcd_sub(num1, num2 - num1)


if __name__ == '__main__':
    import unittest

    class Test(unittest.TestCase):

        def test_gcd(self):
            for func in [gcd_div, gcd_sub]:
                self.assertEqual(func(0, 0), 0)
                self.assertEqual(func(3, 0), 3)
                self.assertEqual(func(0, 2), 2)
                self.assertEqual(func(5, 5), 5)
                self.assertEqual(func(12, 4), 4)
                self.assertEqual(func(24, 18), 6)

    unittest.main()
