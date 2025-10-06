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
     ListNode reverse(ListNode node){
            ListNode prev=null;
            ListNode temp=node;
            while(temp!=null){
                ListNode front = temp.next;
                temp.next=prev;
                prev=temp;
                temp=front;
            }
            return prev;
        }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode first=reverse(l1);
        ListNode second = reverse(l2);
        int carry=0;
        ListNode Newnode = new ListNode(0);
        ListNode temp=Newnode;
        while(first!=null || second!=null){
            int p=carry;
            if(first!=null){
                p+=first.val;
                first=first.next;
            }
            if(second!=null){
                p+=second.val;
                second=second.next;
            }
            temp.next=new ListNode(p%10);
            carry=p/10;
            temp=temp.next;
        }
        if (carry>0){
            ListNode Newnode2=new ListNode(carry);
            temp.next=Newnode2;
            temp=temp.next;
        }
        return reverse(Newnode.next);
    }
    }