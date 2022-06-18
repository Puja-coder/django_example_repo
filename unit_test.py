"""
    imporing MatchingString file to call its function
"""
import unittest
import MatchingString
class Test(unittest.TestCase):

    def test(self):
        text = 'team_stylight'
        my_str = ['helloworld', 'foo', 'team_stylight', 'bar', 'stylight_team', 'seo']
        result =MatchingString.Match(my_str).find_1(text)
        expected_output = ['team_stylight', 'stylight_team']
        # comparing the expected & actual result
        self.assertEqual(result, expected_output)

if __name__=='__main__':
    unittest.main()