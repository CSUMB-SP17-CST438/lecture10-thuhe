import unittest
import random_functions

class ChatbotResponseTest(unittest.TestCase):
    def test_command(self):
        r = random_functions.get_chatbot_response('!! potato')
        self.assertEqual('Woosh', r)

    # def fasdfssdfsdtest_not_a_command(self):


class StringSplitTestCase(unittest.TestCase):
    def test_bat_man(self):
        s = 'bat man'
        result = s.split()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 'bat')
        self.assertEqual(result[1], 'man')

    def test_spaces_string(self):
        result = '        '.split()
        self.assertEqual(len(result), 0)

    # def test_bad_spaces_string(self):
    #     result = '        '.split()
    #     self.assertEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main()