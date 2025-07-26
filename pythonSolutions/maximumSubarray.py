'''
Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''
class Solution(object):
    # Kadane's Algorithm
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best_sum = sum(nums)
        current_sum = 0
        for value in nums:
            current_sum = max(value, current_sum + value)
            best_sum = max(best_sum, current_sum)
        return best_sum