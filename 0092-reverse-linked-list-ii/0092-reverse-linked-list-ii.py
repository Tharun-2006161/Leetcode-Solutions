# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        d=ListNode(0)
        d.next=head
        prev=d
        for i in range(left-1):
            prev=prev.next
        start=prev.next
        current=start.next
        for i in range(right-left):
            temp=current.next
            current.next=prev.next
            prev.next=current
            current=temp
        start.next=current
        current=d.next
        return current
        


        