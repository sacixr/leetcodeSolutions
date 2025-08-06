''' Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

def get_val(listNode):
    try:
        return listNode.val if listNode.val else 0
    except:
        return 0

def get_next(listNode):
    try:
        listNode = listNode.next if listNode.next else None
    except:
        listNode = None
    return listNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        carry = 0

        while True:
            if head.next == None:
                currentNode = head

            nodeVal = get_val(l1) + get_val(l2) + get_val(currentNode)
            carry = 0
            if nodeVal > 9:
                carry = nodeVal // 10
                nodeVal = nodeVal % 10
            currentNode.val = nodeVal
            l1 = get_next(l1)
            l2 = get_next(l2)

            if l1 == None and l2 == None:
                if carry:
                    currentNode.next = ListNode(carry)
                break

            currentNode.next = ListNode(carry)
            currentNode = currentNode.next
        
        return head