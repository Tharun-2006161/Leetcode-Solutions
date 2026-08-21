class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = sorted(zip(position,speed),reverse = True)
        st = []
        for i,j in s:
            p = (target - i) / j
            if not st or p > st[-1]:
                st.append(p)
        return len(st)