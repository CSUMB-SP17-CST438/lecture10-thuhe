import unittest

class StringSplitTestCase(unittest.TestCase):
    def test_bat_man(self):
        s = 'bat man'
        result = s.split()
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()