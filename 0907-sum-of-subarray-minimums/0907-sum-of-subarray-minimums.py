class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        st = [len(arr)] * len(arr)
        sta = []
        for i in range(len(arr)):
            while sta and arr[sta[-1]] >= arr[i]:
                st[sta.pop()] = i
            sta.append(i)
        st1 = [-1] * len(arr)
        sta = []
        for i in range(len(arr)-1, -1, -1):
            while sta and arr[sta[-1]] > arr[i]:
                st1[sta.pop()] = i
            sta.append(i)
        res = 0
        for i in range(len(arr)):
            left = i - st1[i]
            right = st[i] - i
            res += (left * right * arr[i]) 
        return res % MOD
