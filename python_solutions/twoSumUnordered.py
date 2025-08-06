'''Two Sum: Input Array Unsorted
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''

def twoSumUnordered(nums, target):
  # initialize dictionary to store all complement values
  values = {}

  for i in range(len(nums)):
    # calculate the complement, or the difference needed for nums[i] to be the total
    complement = target - nums[i]
    # if the complement is in our dictionary, we have a solution
    if complement in values:
        return [i, values[complement]]
    # else, add it to the dictionary
    values[nums[i]] = i

# If you would like to see this code working, please run the file and make sure you have python installed.
numbers = [2,7,11,15]
target = 9
print("Our numbers are:", numbers, "\nOur target is:", target)
print("Indexes of solution:", twoSumUnordered(numbers, target))

numbers = [3,2,4]
target = 6
print("Our numbers are:", numbers, "\nOur target is:", target)
print("Indexes of solution:", twoSumUnordered(numbers, target))

numbers = [-1, 0]
target = -1
print("Our numbers are:", numbers, "\nOur target is:", target)
print("Indexes of solution:", twoSumUnordered(numbers, target))
        
numbers = [100, -90, 3, 1, 3, 4, 9, 10, 25, -3, 1]
target = -81
print("Our numbers are:", numbers, "\nOur target is:", target)
print("Indexes of solution:", twoSumUnordered(numbers, target))