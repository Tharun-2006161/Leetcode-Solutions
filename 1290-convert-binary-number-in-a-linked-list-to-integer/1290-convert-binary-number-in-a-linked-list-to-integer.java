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
    public int getDecimalValue(ListNode head) {
        ListNode temp = head;
        int decimal=0;
        int base=1;
        String len="";
        while(temp!=null){
            len+=temp.val;
            temp=temp.next;
        }
        for(int i=len.length()-1;i>=0;i--){
            if(len.charAt(i)=='1'){
                decimal+=base;
            }
            base=base*2;
        }
        return decimal;
    }
}