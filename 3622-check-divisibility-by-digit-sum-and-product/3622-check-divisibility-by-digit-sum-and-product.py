class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def sum(n):
            su = 0
            while n > 0:
                r = n % 10
                su = su + r
                n = n // 10
            return su
        def mul(n):
            m = 1
            while n > 0:
                r = n % 10
                m = m * r
                n = n // 10
            return m
        print(sum(n),mul(n))
        
        if n % (sum(n) + mul(n)) == 0:
            return True
        else:
            return False