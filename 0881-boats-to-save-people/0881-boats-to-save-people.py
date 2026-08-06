class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        c = 0
        i = 0
        j = len(people) - 1
        while i < j:
            if people[i] + people[j] > limit:
                j -= 1
                c += 1
            elif people[i] + people[j] <= limit:
                i += 1
                j -= 1
                c += 1
        if i == j:
            c += 1
        return c
