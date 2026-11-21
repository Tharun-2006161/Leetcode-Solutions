class Solution:
    def largestOddNumber(self, num: str) -> str:

        i = len(num) - 1
        num = list(num)
        while i >= 0:
            if int(num[i]) % 2 != 0:
                return "".join(num[:i + 1])
            i -= 1
        return ""
        
