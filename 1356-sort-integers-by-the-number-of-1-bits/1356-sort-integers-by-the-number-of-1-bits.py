class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        arr_sorted = sorted(arr, key=lambda x: (x.bit_count(), x))
        return arr_sorted

