'''Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or str(x) != str(x)[::-1]:
            return False
        return True