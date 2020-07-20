# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node = head
        while node:
            if node.next and node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        if head and head.val == val:
            return head.next
        return head