"""
Recursive way to calculate the factorial of the given number.
"""


def fact(num):
    """
    Returns factorial of a non-negative integer `num`.
    """
    if num == 0:
        return 1

    return num * fact(num - 1)


if __name__ == '__main__':
    import math
    import unittest

    class Test(unittest.TestCase):

        def test_fact(self):
            test_seq = range(15)

            for num in test_seq:
                self.assertEqual(fact(num), math.factorial(num))

    unittest.main()
