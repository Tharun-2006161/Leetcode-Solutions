class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        for i in range(len(seats)):
            if seats[i] - students[i] < 0:
                ans += abs(seats[i] - students[i])
            else:
                ans += (seats[i] - students[i])
        return ans