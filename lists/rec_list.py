"""
Simple manipulations with lists using recursive functions.
"""


def is_member(lst, elem):
    """
    Take `lst` and determines whether `elem` is in `lst`.
    Returns True or False.
    """
    if lst:
        if elem == lst[0]:
            return True
        else:
            return is_member(lst[1:], elem)

    return False


def list_reverse(lst):
    """
    Takes a list and returns a new list whose elements appear
    in reversed order.
    """
    res = []

    if lst:
        res.append(lst[-1])
        res += list_reverse(lst[:-1])

    return res


def slice(lst, first, last):
    """
    Takes a list and returns a corresponding Python list
    slice `lst[first:last]`
    """
    res = []

    if lst:

        if 0 <= first < last <= len(lst):
            res.append(lst[first])
            res += slice(lst, first + 1, last)

    return res


if __name__ == '__main__':
    import unittest

    class Test(unittest.TestCase):

        def test_is_member(self):
            self.assertEqual(is_member([], 1), False)
            self.assertEqual(is_member([1], 1), True)
            self.assertEqual(is_member([3, 14, 15], 14), True)
            self.assertEqual(is_member(['s', 'p', 'a', 'm'], 'a'), True)
            self.assertEqual(is_member(['e', 'g', 'g', 's'], 'i'), False)

        def test_list_reverse(self):
            self.assertEqual(list_reverse([]), [])
            self.assertEqual(list_reverse([1]), [1])
            self.assertEqual(list_reverse([1, 2, 3]), [3, 2, 1])
            self.assertEqual(list_reverse([2, 3, 1]), [1, 3, 2])

            # `test_lst` length is limited by default value of the
            # maximum recursion depth.
            # It is possible to change the recursion limit with
            # `sys.setrecursionlimit`, but it may cause stack
            # overflow.
            test_lst = range(800)
            self.assertEqual(list_reverse(test_lst), test_lst[::-1])

        def test_slice(self):
            self.assertEqual(slice([], 0, 0), [])
            self.assertEqual(slice([1], 0, 0), [])
            self.assertEqual(slice([1], 0, 1), [1])
            self.assertEqual(slice([1, 2, 3], 0, 3), [1, 2, 3])
            self.assertEqual(slice([1, 2, 3], 1, 2), [2])

            # test against built-in slice operator `:`
            import random
            val = 20
            test_lst = range(val)

            for _ in range(100):
                first = random.randrange(val)
                last = random.randrange(val)
                self.assertEqual(slice(test_lst, first, last), test_lst[first:last])

    unittest.main()
