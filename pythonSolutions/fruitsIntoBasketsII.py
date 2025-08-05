'''Fruits Into Baskets II
You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
Each basket can hold only one type of fruit.
If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible allocations are made.'''

class Solution(object):
  def createEmptyArray(self, length):
    array = []
    while len(array) < length:
      array.append(0) 
    return array

  def numOfUnplacedFruits(self, fruits, baskets):
      """
      :type fruits: List[int]
      :type baskets: List[int]
      :rtype: int
      """

      empty = self.createEmptyArray(len(baskets))
      total_fruits = len(fruits)

      for fruit in fruits:
        for index, basket in enumerate(baskets):
          if fruit <= basket and empty[index] == 0:
            empty[index] = fruit
            total_fruits -= 1
            break
    
      return total_fruits