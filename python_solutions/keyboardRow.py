'''Keyboard Row
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
'''

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        final = []

        f_row = "qwertyuiop"
        s_row = "asdfghjkl"
        t_row = "zxcvbnm"

        for word in words:
            s_word = set(word.lower())
            if s_word.issubset(set(f_row)) or s_word.issubset(set(s_row)) or s_word.issubset(set(t_row)):
                final.append(word)
        
        return final