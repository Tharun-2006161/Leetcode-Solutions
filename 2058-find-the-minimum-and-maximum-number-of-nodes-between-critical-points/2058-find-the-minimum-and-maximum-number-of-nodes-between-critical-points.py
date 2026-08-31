# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # arr = []
        # temp = head
        # while temp != None:
        #     arr.append(temp.val)
        #     temp = temp.next
        # i = 0
        # j = 1
        # k = 2
        # mi = []
        # while i < len(arr) and j < len(arr) and k < len(arr):
        #     if (arr[j] > arr[i] and arr[j] > arr[k]):
        #         mi.append(j + 1)
        #     elif (arr[j] < arr[i] and arr[j] < arr[k]):
        #         mi.append(j + 1)
        #     i += 1
        #     j += 1
        #     k += 1
        # print(mi)
        # mini = float(inf)
        # i = 0
        # j = 1
        # while i < len(mi) and j < len(mi):
        #     mini = min(mini, abs(mi[i] - mi[j]))
        #     i += 1
        #     j += 1
        # maxi = 0
        # if len(mi) >= 2:
        #     maxi = mi[-1] - mi[0]
        # if mini != float('inf') and maxi:
        #     return [mini, maxi]
        # else:
        #     return [-1, -1]
        temp = head
        cnt = 1
        res = []
        while temp != None and temp.next != None and temp.next.next != None:
            a = temp.val
            b = temp.next.val
            c = temp.next.next.val
            if (a > b and c > b) or (a < b and c < b):
                res.append(cnt + 1)
            cnt += 1
            temp = temp.next
        print(res)
        mi = float('inf')
        i = 0
        j = 1
        while i < len(res) and j < len(res):
            mi = min(mi, abs(res[i] - res[j]))
            i += 1
            j += 1
        if len(res) >= 2:
            ma = res[-1] - res[0]
        if mi != float('inf') and ma:
            return [mi, ma]
        else:
            return [-1, -1]
