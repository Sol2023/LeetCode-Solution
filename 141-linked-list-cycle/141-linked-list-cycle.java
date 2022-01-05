/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode current = head;
        Set<ListNode> seen = new LinkedHashSet<>();
        while(current != null) {
            if(seen.contains(current))  return true;
            seen.add(current);
            current=current.next;
        }
        return false;
        
    }
}