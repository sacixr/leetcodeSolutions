'''Fruit Into Baskets
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
'''
class Solution(object):
    def calculateTotalFruit(self, fruits_dict):
        total = 0
        for fruit in iter(fruits_dict):
            total += fruits_dict[fruit]
        return total
        
    def totalFruit(self, fruits):
        max_fruit = 0
        other_fruit = {}
        left = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            other_fruit[fruit] = other_fruit.get(fruit, 0) + 1

            while len(other_fruit) > 2:
                left_fruit = fruits[left]
                other_fruit[left_fruit] -= 1
                if other_fruit[left_fruit] == 0:
                    del other_fruit[left_fruit]
                left += 1

            max_fruit = max(max_fruit, self.calculateTotalFruit(other_fruit))

        return max_fruit