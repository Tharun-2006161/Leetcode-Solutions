# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        f=l1
        s=l2
        m=ListNode()
        temp=m
        carry=0
        while f is not None and s is not None:
            p=f.val+s.val+carry
            digits=p%10
            carry=p//10
            newnode = ListNode(digits)
            temp.next=newnode
            temp=temp.next
            f=f.next
            s=s.next
        while f is not None:
            p=f.val+carry
            digits=p%10
            carry=p//10
            newnode=ListNode(digits)
            temp.next=newnode
            temp=temp.next
            f=f.next
        while s is not None:
            p=s.val+carry
            digits=p%10
            carry=p//10
            newnode=ListNode(digits)
            temp.next=newnode
            temp=temp.next
            s=s.next
        if carry>0:
            li=ListNode(carry)
            temp.next=li
        return m.next
        