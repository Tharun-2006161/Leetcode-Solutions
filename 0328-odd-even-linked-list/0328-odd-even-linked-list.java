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
        ListNode temp=head;
        ListNode Newnode = new ListNode(0);
        ListNode Newnode1 = new ListNode(0);
        ListNode Odd=Newnode;
        ListNode Even=Newnode1;
        int count=1;
        while(temp!=null){
            if (count%2!=0){
                Odd.next=temp;
                Odd=Odd.next;
            }
            else{
                Even.next=temp;
                Even=Even.next;
            }
            temp=temp.next;
            count++;
        }
            
        
        Odd.next=Newnode1.next;
        Even.next=null;
        return Newnode.next;
    }
}