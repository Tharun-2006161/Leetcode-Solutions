class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:

        def c_s(arr):
            c = [0] * (max(arr) + 1)
            for i in arr:
                c[i] += 1
            res = []
            for i in range(len(c)):
                res.extend([i] * c[i])
            return res
        seats = c_s(seats)
        students = c_s(students)
        ans = 0
        for i in range(len(seats)):
            if seats[i] - students[i] < 0:
                ans += abs(seats[i] - students[i])
            else:
                ans += (seats[i] - students[i])
        return ans