class Solution:
    def getLucky(self, s: str, k: int) -> int:

        def fun(a,k):
            while k > 0:
                su = 0
                while a > 0:
                    r = a % 10
                    su = su + r
                    a = a // 10
                a = su
                k -= 1
            return a
                
        p = ""
        for i in s:
            p += str((ord(i) - ord('a')) + 1)
        return (fun(int(p) , k))