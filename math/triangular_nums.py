"""
Triangular numbers.
"""


def triangular_sum(num):
    """
    Returns the 'n'th triangle number.
    Corresponds to the number of dots composing a triangle with
    n dots on a side, and is equal to the sum of the n natural
    numbers from 1 to n.
    """
    if num == 0:
        return 0

    return triangular_sum(num - 1) + num


if __name__ == '__main__':
    import unittest

    class Test(unittest.TestCase):

        def test_triangular_sum(self):
            ref_func = lambda n: n * (n + 1) / 2

            for i in range(50):
                self.assertEqual(triangular_sum(i), ref_func(i))

    unittest.main()
