# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next=head
        cur=dummy
        temp=dummy
        count=0
        
        while temp.next:
            count+=1
            temp=temp.next 
        
        idx = count-n
        
        while idx>0:
            cur=cur.next 
            idx-=1
        
        cur.next=cur.next.next
        
        return dummy.next
            