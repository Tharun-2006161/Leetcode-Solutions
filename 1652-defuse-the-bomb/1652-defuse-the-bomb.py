class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        if k < 0:
            res = code[k:] + code
            prefix = [0] * len(res)
            p = 0
            print(res)
            for i in range(len(prefix)):
                p += res[i]
                prefix[i] = p
            l = 0
            print(prefix)
            res1 = [0] * len(code)
            i = abs(k)
            while i < len(prefix) :
                if l > 0:
                    res1[l] = (prefix[i - 1] - prefix[l - 1])
                else:
                    res1[l] = prefix[i - 1]
                l += 1
                i += 1
            return res1
        if k > 0:
            res = code + code[:k]
            p = 0
            for i in range(len(res)):
                p += res[i]
                res[i] = p
            res1 = [0] * len(code)
            l = 0
            i = k
            while i < len(res):
                res1[l] = res[i] - res[l]
                l += 1
                i += 1
            return res1
        if k == 0:
            return [0] * len(code)