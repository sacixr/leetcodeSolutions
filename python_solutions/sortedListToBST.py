'''Convert Sorted List to Binary Search Tree
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.
'''

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def recursive(self, array):
    if len(array) == 1:
      return TreeNode(array[0])

    half = len(array) // 2
    right = array[-half:]

    if half == len(array)-1:
      return TreeNode(
        val=array[half],
        left=self.recursive(array[:half]),
        right=None,
      )
    elif half == 0:
      return TreeNode(
        val=array[half],
        left=None,
        right=self.recursive(right),
      )

    if len(array) % 2 == 0:
      right = array[-(half-1):]

    return TreeNode(
      val=array[half],
      left=self.recursive(array[:half]),
      right=self.recursive(right)
    )

  def sortedListToBST(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[TreeNode]
    """
    linkedarray = []

    if not head:
      return None

    # you could say i'm being slightly cheeky as i ultimately convert the linked list to an array, but i found this way simpler :)
    while True:
      linkedarray.append(head.val)
      if head.next == None:
        break
      head = head.next
  
    return self.recursive(linkedarray)
