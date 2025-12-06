'''Reformat The String
You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.
'''

class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """

        letters = [char for char in s if char.isalpha()]
        integers = [char for char in s if char.isdigit()]
        
        if (not letters and not integers) or len(letters) < len(integers)-1 or len(integers) < len(letters)-1:
            return ""
        
        longer = max(letters, integers, key=len)
        shorter = min(integers, letters, key=len)
        index = 0
        result = ""

        while index < len(shorter):
            result += longer[index] + shorter[index]
            index += 1
        
        if len(longer) > len(shorter):
            result += longer[-1:][0]

        return result