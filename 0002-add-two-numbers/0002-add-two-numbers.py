# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        lst1 = l1
        lst2 = l2
        dummy = ListNode()
        temp = dummy
        carry = 0
        while lst1 != None and lst2 != None:
            s = lst1.val + lst2.val + carry
            digits = s % 10
            carry = s // 10
            newnode = ListNode(digits)
            temp.next = newnode
            temp = temp.next
            lst1 = lst1.next
            lst2 = lst2.next
        while lst1 != None:
            s = lst1.val + carry
            digits = s % 10
            carry = s // 10
            newnode = ListNode(digits)
            temp.next = newnode
            temp = temp.next
            lst1 = lst1.next
        while lst2 != None:
            s = lst2.val + carry
            digits = s % 10
            carry = s // 10
            newnode = ListNode(digits)
            temp.next = newnode
            temp = temp.next
            lst2 = lst2.next
        if carry > 0:
            temp.next = ListNode(carry)
        return dummy.next