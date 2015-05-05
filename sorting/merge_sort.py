"""
Implementation of top-down merge sort algorithm. Recursively
splits the list into sublists until sublist size is 1, then
merges those sublists to produce a sorted list.
"""


def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    Usage of sets or python built-in sorting functions avoided.
    """
    lst1 = list1[:]
    lst2 = list2[:]
    res = []

    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            item = lst1.pop(0)
        else:
            item = lst2.pop(0)

        res.append(item)

    if lst1:
        res.extend(lst1)
    else:
        res.extend(lst2)

    return res


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as `list1`.
    """
    if len(list1) <= 1:
        return list1

    mid = len(list1) / 2
    left = list1[:mid]
    right = list1[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


if __name__ == '__main__':
    import random
    import unittest

    class Test(unittest.TestCase):

        def setUp(self):
            self.lst1 = [random.randrange(1000) for _ in range(100)]
            self.lst2 = [random.randrange(1000) for _ in range(100)]

        def test_merge(self):
            self.assertEqual(merge([8], [3]), [3, 8])
            self.assertEqual(merge([], [2]), [2])

            self.lst1.sort()
            self.lst2.sort()

            res = self.lst1 + self.lst2
            self.assertEqual(merge(self.lst1, self.lst2), sorted(res))

        def test_merge_sort(self):
            self.assertEqual(merge_sort(self.lst1), sorted(self.lst1))
            self.assertEqual(merge_sort(self.lst2), sorted(self.lst2))

    unittest.main()
