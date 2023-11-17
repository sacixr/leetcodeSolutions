'''Two Sum: Input Array Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.'''

def twoSum(numbers, target):
    # set left to be at the beginning of the array
    left = 0
    # set right to be the very end of the array
    right = len(numbers)-1

    # while the total of the two numbers isn't the target
    while numbers[left] + numbers[right] != target:
        # if the total of the two numbers is larger than the target
        if numbers[left] + numbers[right] > target:
            # move the right pointer down (as we know we are adding too much)
            right-=1
        else:
            # else, we know we aren't adding enough, so increment left
            left+=1
    
    # return the index of both the left and right data which adds up to the solution
    return [left+1, right+1]

# If you would like to see this code working, please run the file and make sure you have python installed.
numbers = [2,7,11,15]
target = 9
print("Our numbers are:", numbers, "\nOur target is:", target)
print("Indexes of solution:", twoSum(numbers, target))

numbers = [2,3,4]
target = 6
print("Our numbers are:", numbers, "\nOur target is:", target)
print("Indexes of solution:", twoSum(numbers, target))

numbers = [-1, 0]
target = -1
print("Our numbers are:", numbers, "\nOur target is:", target)
print("Indexes of solution:", twoSum(numbers, target))
        
numbers = [0,0,3,4]
target = 0
print("Our numbers are:", numbers, "\nOur target is:", target)
print("Indexes of solution:", twoSum(numbers, target))