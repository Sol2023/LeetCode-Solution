/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if(head ==null || head.next==null) return head;
        ListNode oddHead = null;
        ListNode oddTail = null;
        ListNode evenHead = null;
        ListNode evenTail = null;
        ListNode curNode = head;
        int pointer = 1;
        
        while(curNode != null){
            if(pointer%2==1){
                if(oddHead == null){
                    oddHead = curNode;
                    oddTail = curNode;
                } else {
                    oddTail.next = curNode;
                    oddTail = oddTail.next;
                }
            } else{
                if(evenHead == null){
                    evenHead = curNode;
                    evenTail = curNode;
                } else{
                    evenTail.next = curNode;
                    evenTail = evenTail.next;
                }
            }
            
            curNode = curNode.next;
            pointer++;
        }
        
        evenTail.next = null;
        oddTail.next = evenHead;
        
        return oddHead;
        
    }
}