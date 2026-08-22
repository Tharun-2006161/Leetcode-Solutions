class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        if flowerbed[0] == 0 and flowerbed[1] == 0 and n > 0:
            flowerbed[0] = 1
            n -= 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0 and n > 0:
            flowerbed[-1] = 1
            n -= 1
        i = 2
        while i < len(flowerbed) and (i + 1) < len(flowerbed):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and n > 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
            i += 1
        return n == 0