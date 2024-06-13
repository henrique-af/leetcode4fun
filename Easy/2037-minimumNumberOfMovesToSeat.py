from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        total = 0

        for seat, student in zip(seats, students):
            total += abs(seat - student)
        return total


seats = [3, 1, 5]
students = [2, 7, 4]
