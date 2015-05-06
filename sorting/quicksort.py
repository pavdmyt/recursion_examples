"""
Implementation of quicksort algorithm. Divides a large array into two
smaller sub-arrays: the low elements and the high elements.
Quicksort then recursively sorts the sub-arrays.
"""


def quick_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as `list1`.
    """
    if not list1:
        return []

    pivot = list1[0]
    low_elem = [num for num in list1 if num < pivot]
    pivots = [num for num in list1 if num == pivot]
    high_elem = [num for num in list1 if num > pivot]

    return quick_sort(low_elem) + pivots + quick_sort(high_elem)


if __name__ == '__main__':
    import random
    import unittest

    class Test(unittest.TestCase):

        def setUp(self):
            self.lst1 = [random.randrange(1000) for _ in range(100)]
            self.lst2 = [random.randrange(1000) for _ in range(100)]

        def test_quick_sort(self):
            self.assertEqual(quick_sort(self.lst1), sorted(self.lst1))
            self.assertEqual(quick_sort(self.lst2), sorted(self.lst2))

    unittest.main()
