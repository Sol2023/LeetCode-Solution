# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None: return head
        oddHead = None
        oddTail = None
        evenHead = None
        evenTail = None
        current = head
        i = 1
        
        while current!=None:
            if i%2==1:
                if oddHead == None:
                    oddHead = current
                    oddTail = current
                else: 
                    oddTail.next = current
                    oddTail = oddTail.next
            else:
                if evenHead == None:
                    evenHead = current
                    evenTail = current
                else:
                    evenTail.next=current
                    evenTail = evenTail.next
            
            current = current.next
            i+=1
        
        evenTail.next= None
        oddTail.next = evenHead
        
        return oddHead
                
                
        
        