# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head:ListNode):
        if not head or not head.next:
            return head
        newhead= head.next
        head.next=self.swapPairs(newhead.next)
        newhead.next=head
        return newhead