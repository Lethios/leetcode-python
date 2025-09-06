# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        queue = deque()

        carry = 0
        head, current_node = None, None
        while l1 or l2 or carry > 0:
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0
            
            digit = num1 + num2 + carry
            carry = digit // 10
            digit = digit % 10

            queue.append(digit)

        head = queue.popleft()
        head = ListNode(head)
        current_node = head
        while queue:
            num = queue.popleft()
            current_node.next = ListNode(num)
            current_node = current_node.next

        return head
