class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        st = []
        res = prices.copy()
        print(res)
        for i in range(len(prices) - 1, -1, -1):
            while st and st[-1] > prices[i]:
                st.pop()
            if st:
                res[i] = prices[i] - st[-1]
            st.append(prices[i])
        return res
