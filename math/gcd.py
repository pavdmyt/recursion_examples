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


def gcd_bin(num1, num2):
    """
    Takes two non-negative integers and returns greatest
    common divisor of these numbers.

    Implementation of binary GCD algorithm:
    gcd(a, 0) = a, gcd(0, b) = b, gcd(0, 0) = 0
    gcd(a, b) = gcd(a/2, b)         if a is even and b is odd
    gcd(a, b) = gcd(a, b/2)         if a is odd and b is even
    gcd(a, b) = 2 * gcd(a/2, b/2)   if a is even and b is even
    gcd(a, b) = gcd((a - b)/2, b)   if a is odd and b is odd and a > b
    gcd(a, b) = gcd((b - a)/2, a)   if a is odd and b is odd and a <= b
    """
    if num1 * num2 == 0:
        return num1 + num2

    # num1, num2 or both are even
    if num1 % 2 == 0:

        if num2 % 2 != 0:
            return gcd_bin(num1 >> 1, num2)  # bit shifting: a >> 1 = a / 2
        else:
            return gcd_bin(num1 >> 1, num2 >> 1) << 1  # a << 1 = a * 2

    if num2 % 2 == 0:
        return gcd_bin(num1, num2 >> 1)

    # both num1 and num2 are odd
    if num1 > num2:
        return gcd_bin((num1 - num2) >> 1, num2)

    return gcd_bin((num2 - num1) >> 1, num1)


if __name__ == '__main__':
    import unittest

    class Test(unittest.TestCase):

        def test_gcd(self):
            for func in [gcd_div, gcd_sub, gcd_bin]:
                self.assertEqual(func(0, 0), 0)
                self.assertEqual(func(3, 0), 3)
                self.assertEqual(func(0, 2), 2)
                self.assertEqual(func(4, 4), 4)
                self.assertEqual(func(5, 5), 5)
                self.assertEqual(func(12, 4), 4)
                self.assertEqual(func(15, 10), 5)
                self.assertEqual(func(10, 15), 5)
                self.assertEqual(func(21, 7), 7)
                self.assertEqual(func(7, 21), 7)
                self.assertEqual(func(24, 18), 6)

    unittest.main()
