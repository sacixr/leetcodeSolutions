''' 
Majority Element Problem.
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than [n / 2] times. You may assume that the majority element always exists in the array. '''

def majorityElement(nums) -> int:
    # sort the values in the array so the are in ascending order
    nums.sort()
    # as majority element is always the value which appears more than n/2 times, we know that once sorted,
    # the majority element will take up the n/2 position, or the halfway position
    half = len(nums) // 2
    # return that position
    return nums[half]

# If you would like to see this code working, please run the file and make sure you have python installed.
nums = [3,2,3]
print("If nums = ", nums)
print("Majority Element is:", majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print("If nums = ", nums)
print("Majority Element is:", majorityElement(nums))

nums = [1,5,5,2,3,8,5,1,8,5,5,5,4,5,5,5]
print("If nums = ", nums)
print("Majority Element is:", majorityElement(nums))