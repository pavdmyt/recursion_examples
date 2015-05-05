"""
Simple manipulations with strings using recursive functions.
"""


def remove_char(my_str, char):
    """
    Takes a string `my_str` and removes all instances of
    the character `char` from the string.
    """
    assert len(char) <= 1, 'Character length >1 !'

    if not my_str:
        return ''

    tail = remove_char(my_str[1:], char)

    if my_str[0] != char:
        return my_str[0] + tail

    return tail


def insert_char(my_str, char):
    """
    Adds the character `char` between each pair of consecutive characters
    in the `my_str`.
    """
    res = ''

    if len(my_str) < 2:
        res += my_str
    else:
        res += my_str[0]
        res += char
        res += insert_char(my_str[1:], char)

    return res


if __name__ == '__main__':
    import unittest

    class Test(unittest.TestCase):

        def test_remove_char(self):
            self.assertEqual(remove_char('', ''), '')
            self.assertEqual(remove_char('spam', ''), 'spam')
            self.assertEqual(remove_char('drwxrwxr-x', 'd'), 'rwxrwxr-x')
            self.assertEqual(remove_char('drwxrwxr-x', 'x'), 'drwrwr-')

            with self.assertRaises(AssertionError):
                remove_char('drwxrwxr-x', 'rw')

        def test_insert_char(self):
            self.assertEqual(insert_char('', 'x'), '')
            self.assertEqual(insert_char('eggs', ''), 'eggs')
            self.assertEqual(insert_char('c', 'x'), 'c')
            self.assertEqual(insert_char('foo', 'x'), 'fxoxo')
            self.assertEqual(insert_char('catdog', 'x'), 'cxaxtxdxoxg')
            self.assertEqual(insert_char('0000', '11'), '0110110110')

    unittest.main()
