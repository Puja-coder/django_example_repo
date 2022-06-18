# Find matching strings from a list of given strings without considering the order of the characters.

class Match:
    """
        class to find matching strings from a list of given strings without considering the order of the characters
    """
    def __init__(self, my_list):
        """
            constructor function to initializing param my_list: list of strings
        """
        self.my_list = my_list

    """ Time complexity is a measurement of computing time that an algorithm takes to complete.
        Explanation for find_1(), find_2() functions:
                time complexity of len(), set() & append() : O(1)
                time complexity of for-loop : O(n)
                time complexity of nested 2 for-loop (n*n) : O(n^2)
                The if-clause has a time complexity : O(1), and the else-clause has a time complexity : O(n),
                if if-clause & else-clause is inside the for-loop, the entire method has a time complexity : O(n)

        Space complexity is the measurement of memory (space) that an algorithm needs.
        Explanation for find_1(), find_2() functions:
                space complexity of for-loop: O(n)
                space complexity of Creating and assigning values to variables is: O(1)
                space complexity while calling functions: O(n)
                space complexity of return value: O(1)
    """
    # Time complexity of find_1() is less than Time complexity of find_2().

    # Method 1: convert string (list item & given string) to set and compare
    def find_1(self, my_str):
        """
            initializing param my_str: string to find in list
            return:list of matched string
            Time complexity :-
                Best Case: O(1) Time
                Average Case: O(1) Time
                Worst Case: O(n) Time
            Space complexity :- O(n)
        """
        self.my_str = my_str
        result = []
        for item in self.my_list:
            # if length of string doesnt match, jump to next iteration.
            if len(item) != len(self.my_str):
                continue
            else:
                if set(item) == set(self.my_str):
                    result.append(item)
        return result

    # Method 2: Sort the string item and compare
    def find_2(self, my_str):
        """
                Time complexity :-
                    Best Case: O(n^2) Time
                    Average Case: O(n^2) Time
                    Worst Case: O(n^2) Time
        """
        self.my_str = my_str
        sorted_str = self.sorting(self.my_str)
        result = []
        for item in self.my_list:  # n
            if len(item) != len(self.my_str):
                continue
            else:
                # Calling sorting() function to sort the list item & given string
                if self.sorting(item) == sorted_str:
                    result.append(item)
        return result

    # Sort Function
    def sorting(self, string):
        """
            initializing param: string
            return: list of sorted string item
            Time complexity :-
                Best Case: O(n^2) Time
                Average Case: O(n^2) Time
                Worst Case: O(n^2) Time
        """
        self.string = string
        string_items = list(self.string)
        n = len(string_items)
        for i in range(n):
            for j in range(i + 1, n):
                # Comparing with adjacent item & swapping
                if string_items[i] > string_items[j]:
                    string_items[i], string_items[j] = string_items[j], string_items[i]
        return string_items


# Input: list of items
my_list = ['helloworld', 'foo', 'team_stylight', 'bar', 'stylight_team', 'seo']

# Input: item to find
my_str = 'team_stylight'

# Creating object
Match_obj = Match(my_list)

# Calling find_1() function to get the result
print(Match_obj.find_1(my_str))

# Calling find_2() function to get the result
print(Match_obj.find_1(my_str))

# Output for both print statement: ['team_stylight', 'stylight_team']
