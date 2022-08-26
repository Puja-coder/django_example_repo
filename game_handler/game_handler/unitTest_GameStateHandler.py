import unittest
import game_state_handler

# Creating object from class
GameStateHandler_obj = game_state_handler.GameStateHandler()

class Test(unittest.TestCase):

    def test_word(self):
        # comparing new generated file with expected output file
        expected_result =GameStateHandler_obj.parse_files('output/expected_output.json')
        result =GameStateHandler_obj.main()
        self.assertEqual(result, expected_result)

if __name__=='__main__':
    unittest.main()