class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True
        st = []
        for i in nums:
            if st:
                if i > st[-1]:
                    inc = False
                if i < st[-1]:
                    dec = False
            st.append(i)
        return inc or dec