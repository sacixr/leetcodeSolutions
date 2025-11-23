'''Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ["(", "[", "{"]
        right = [")", "]", "}"]

        q = []

        for bracket in s:
            if bracket in left:
                q.append(bracket)
            else:
                index = right.index(bracket)
                if left[index] not in q:
                    return False
                elif q[len(q)-1] == left[index]: 
                    q.pop()
                else:
                    return False
        
        if len(q) >= 1:
            return False

        return True



        