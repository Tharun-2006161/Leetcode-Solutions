class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hash_table = {}

        for i in range(len(s)):
            
            if s[i] not in hash_table:
                hash_table[s[i]] = [i]
            else:
                hash_table[s[i]].append(i)

        m = 0
        for i,j in hash_table.items():

            if len(j) >= 2:
                m=max(m,j[-1] - j[0])

        return m-1