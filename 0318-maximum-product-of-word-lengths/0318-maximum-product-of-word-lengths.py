class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        ma = 0
        masks = []
        for i in words:
            mask = 0
            for j in i:
                bit = ord(j) - ord('a')
                mask |= (1 << bit)
            masks.append(mask)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if masks[i] & masks[j] == 0:
                    ma = max(ma, len(words[i]) * len(words[j]))
        return ma
