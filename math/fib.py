"""
Recursive way to calculate Fibonacci numbers.
"""


def fib(num):
    """
    Takes non-negative integer `num` and returns corresponding
    member from Fibonacci sequence:

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    """
    if num <= 1:
        return num

    return fib(num - 1) + fib(num - 2)


def memo_fib(num, memo_dict={0: 0, 1: 1}):
    """
    Optimized version of `fib`. Already computed values are stored
    in `memo_dict` for later use.

    Time complexity:

    `fib`         O(2^n)
    `memo_dict`   O(2n)
    """
    if num in memo_dict:
        return memo_dict[num]

    prev1 = memo_fib(num - 1, memo_dict)
    prev2 = memo_fib(num - 2, memo_dict)
    memo_dict[num] = prev1 + prev2

    return prev1 + prev2


if __name__ == '__main__':
    import unittest

    def ref_fib(num):
        """
        Reference function for Fibonacci numbers calculation.
        """
        a, b = 1, 0

        for _ in range(num):
            a, b = b, a + b

        return b

    class Test(unittest.TestCase):

        def test_fib(self):
            for func in [fib, memo_fib]:
                self.assertEqual(func(0), ref_fib(0))
                self.assertEqual(func(1), ref_fib(1))
                self.assertEqual(func(5), ref_fib(5))
                self.assertEqual(func(8), ref_fib(8))
                self.assertEqual(func(10), ref_fib(10))

    unittest.main()
