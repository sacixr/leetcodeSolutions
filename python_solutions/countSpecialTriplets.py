'''Count Special Triplets
You are given an integer array nums.

A special triplet is defined as a triplet of indices (i, j, k) such that:

0 <= i < j < k < n, where n = nums.length
nums[i] == nums[j] * 2
nums[k] == nums[j] * 2
Return the total number of special triplets in the array.

Since the answer may be large, return it modulo 109 + 7.
'''

from typing import Counter

class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        prev = Counter(nums[:1])
        after = Counter(nums[1:])

        for item in nums[1:]:
            after[item] -= 1
            count += (prev[item*2] * after[item*2])
            prev[item] += 1
    
        return count % (10**9 + 7)
            