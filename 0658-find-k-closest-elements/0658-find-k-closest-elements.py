class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        lst = arr[:k]
        for i in range(k,len(arr)):
            front = abs(x - arr[i - k])
            back = abs(x - arr[i])
            if front > back:
                lst.append(arr[i])
                lst.remove(arr[i - k])
        return lst