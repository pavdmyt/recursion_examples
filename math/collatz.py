"""
Collatz problem:

- If the number is even, divide it by two.
- If the number is odd, triple it and add one.
(number is an arbitrary positive integer).

The Collatz conjecture:

This process will eventually reach the number 1, regardless
of which positive integer is chosen initially.
"""


def collatz(num, steps=0):
    """
    f(n) = n/2     if n is even
    f(n) = 3n + 1  if n is odd
    n is natural number

    No matter what number you start with,
    you will always eventually reach 1.

    Returns number of iterations of this reduction.
    """
    if num == 1:
        return num, steps
    elif num % 2 == 0:
        return collatz(num / 2, steps + 1)
    else:
        return collatz(num * 3 + 1, steps + 1)


if __name__ == '__main__':
    import unittest

    class Test(unittest.TestCase):

        def test_collatz(self):
            # the sequence for n=27 takes 111 steps
            self.assertEqual(collatz(27), (1, 111))

            # the longest progression for any initial starting number
            # less than 100 million is 63,728,127, which has 949 steps
            self.assertEqual(collatz(63728127), (1, 949))

            # for starting numbers less than 1 billion
            # it is 670,617,279, with 986 steps
            import sys
            sys.setrecursionlimit(1100)
            self.assertEqual(collatz(670617279), (1, 986))

    unittest.main()
