    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return  
        def reverse(l):
            prev = None
            temp = l
            while temp != None:
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
            return prev
        first = head
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # second = slow.next
        second = reverse(slow.next)
        slow.next = None
        
        while first != None and second != None:
            fnext = first.next
            snext = second.next
            first.next = second
            second.next = fnext
            first = fnext
            second = snext
        