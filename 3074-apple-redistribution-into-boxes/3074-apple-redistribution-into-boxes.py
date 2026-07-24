class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        print(capacity)
        i = 0
        j = 0
        c = 0
        while i < len(apple):
            while i < len(apple) and capacity[j] > 0:
                if apple[i] <= capacity[j]:
                    print(capacity[j],apple[i])
                    capacity[j] = (capacity[j] - apple[i])
                    print(capacity[j])
                    i += 1
                else:
                    apple[i] -= capacity[j]
                    capacity[j] = 0
            j += 1
            c += 1
            
            
        return c
