# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack = deque()

        current_node = l1
        while current_node:
            stack.append(current_node.val)
            current_node = current_node.next
        
        num1 = ""
        while stack:
            num1 += str(stack.pop())

        current_node = l2
        while current_node:
            stack.append(current_node.val)
            current_node = current_node.next

        num2 = ""
        while stack:
            num2 += str(stack.pop())

        num = str(int(num1) + int(num2))

        head_node = ListNode(int(num[-1]))
        current_node = head_node
        for digit in num[-2::-1]:
            current_node.next = ListNode(int(digit))
            current_node = current_node.next

        return head_node
