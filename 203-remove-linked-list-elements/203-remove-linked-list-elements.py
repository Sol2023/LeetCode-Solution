# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next=head
        currentNode =dummy
        while currentNode.next:
            if currentNode.next.val == val:
                currentNode.next = currentNode.next.next
            
            else:
                currentNode = currentNode.next
        
        return dummy.next
    