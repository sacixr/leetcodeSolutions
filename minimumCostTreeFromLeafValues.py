'''Minimum Cost Tree From Leaf Values
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

A node is a leaf if and only if it has zero children.
'''

class Solution:
    def mctFromLeafValues(self, arr):
        total = 0
        st = ['inf']

        for a in arr:
            while st[-1] <= a:
                tmp = st.pop()
                total += tmp * min(a, st[-1])
            st.append(a)

        f = st.pop()
        while len(st) > 1:
            total += f * st[-1]
            f = st.pop()
        
        return total