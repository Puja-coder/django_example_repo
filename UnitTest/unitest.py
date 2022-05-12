import unittest
import code_for_testing
class Test(unittest.TestCase):

    def test_word(self):
        text = 'puja'
        result =code_for_testing.script_for_unit_testing(text)
        self.assertEqual(result, 'Puja')

if __name__=='__main__':
    unittest.main()