'''Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.'''
class Solution(object):
    def recursive(self, nums, target, left, right):
        midway = (left + right) // 2

        if len(nums) == 1 and nums[0] == target:
            return [0,0]
 
        if left > right:
            return [-1, -1]
        
        if target == nums[midway]:
            left = midway
            right = midway
            while left-1 >= 0 and target == nums[left-1]:
                left -= 1
            while right+1 < len(nums) and target == nums[right+1]:
                right += 1
            return[left, right]
        
        if target > nums[midway]:
            return self.recursive(nums, target, midway + 1, right)

        if target < nums[midway]:
            return self.recursive(nums, target, left, midway - 1)

        return [-1, -1]

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(nums)-1
        
        return self.recursive(nums, target, left, right)
