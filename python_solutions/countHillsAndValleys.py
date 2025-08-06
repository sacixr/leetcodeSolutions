'''Count Hills and Valleys in an Array
You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

Return the number of hills and valleys in nums.'''

# my solution beats 100% of other solutions in runtime and 88.64% in memory ! c:
class Solution(object):
  def countHillValley(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    total = 0
    left_index = 0
    mid_index = 1
    right_index = 2

    while right_index <= len(nums)-1:
      while nums[mid_index] == nums[right_index] and right_index+1 <= len(nums)-1:
        right_index += 1

      if (nums[left_index] > nums[mid_index] and nums[right_index] > nums[mid_index]) or (nums[left_index] < nums[mid_index] and nums[right_index] < nums[mid_index]):
        total += 1
      
      if mid_index != right_index-1:
        mid_index = right_index
        left_index = right_index-1
        right_index = right_index+1
      else:
        left_index += 1
        right_index += 1
        mid_index += 1
    
    return total
  
  # the below was my original solution, but this one unnecessarily looped through the entire array, so the above is my more efficient solution  
  def countHillValleyInefficient(self, nums):
    left_index = nums[index-1]
    right_index = nums[index+1]
    for index, num in enumerate(nums):
      if index == 0 or index == len(nums)-1:
        continue

      left_index = nums[index-1]
      right_index = nums[index+1]

      while nums[index] == nums[index+1] and index+1 < len(nums)-1:
        index += 1
        right_index = nums[index+1]

      if (left_index > nums[index] and right_index > nums[index]) or (left_index < nums[index] and right_index < nums[index]):
        total += 1

    return total