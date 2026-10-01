class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        while n:
            a, b = b , a + b
            n -= 1
        return a