# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        s = []
        for i in range(len(lists)):
            temp = lists[i]
            while temp != None:
                s.append(temp.val)
                temp = temp.next
        s.sort()
        dummy = ListNode(0)
        temp = dummy
        i = 0
        while i < len(s):
            temp.next = ListNode(s[i])
            temp = temp.next
            i += 1
        return dummy.next