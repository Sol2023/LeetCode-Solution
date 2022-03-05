# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        f=l1
        s=l2
        curr = dummyHead
        carry =0
        
        while f or s:
            if f is not None:
                x=f.val
            else:
                x=0
            if s is not None:
                y=s.val
            else: 
                y= 0
            total =carry + x + y
            carry = total//10
            curr.next = ListNode(total%10)
            curr =curr.next
            
            if f is not None: f=f.next
            if s is not None: s=s.next
        
        if carry >0:
            curr.next = ListNode(carry)
        
        return dummyHead.next
            
        