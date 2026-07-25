class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:

        # i = k
        # j = num
        # res1 = []
        # res2 = []
        # while i < j:
        #     if i % 10 == k:
        #         res1.append(i)
        #         i += k
        #     i += 1
        #     if j % 10 == k:
        #         res2.append(j)
        #         j -= k
        #     j -= 1
        # print(res1,res2)
        # print(sum(res1),sum(res2))
        # if num == 0:
        #     return 0
        # res = []
        # for i in range(k , num , k+1):
        #     if i % 10 == k:
        #         res.append(i)
        # i = 0
        # j = len(res) - 1
        # c = 0
        # while i < j:
        #     if res[i] + res[j] == num:
        #         c += 1
        #     i += 1
        #     j -= 1
        # if c :
        #     return c
        # else:
        #     return -1
        if num == 0:
            return 0
        for i in range(1,11):
            if ((i * k) % 10 == num % 10) and (i * k) <= num:
                return i
        return -1