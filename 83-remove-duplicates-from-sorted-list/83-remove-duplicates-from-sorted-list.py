# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        
        while currentNode is not None:
            nextNode = currentNode.next
            while nextNode is not None and currentNode.val == nextNode.val:
                nextNode = nextNode.next
            
            currentNode.next = nextNode
            currentNode =nextNode
        
        return head