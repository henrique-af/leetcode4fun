from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        j = len(capacity) - 1
        n = 0
        t_apple = 0 
        count = 0

        for i in range(len(apple)):
            t_apple += apple[i]

        for n in range(len(capacity)):
            while t_apple != 0:
                t_apple = t_apple - capacity[j]
                count += 1
                if t_apple < 0:
                    t_apple = 0
                j = j - 1
            n = n + 1

        return count

    # better way
    def minimumBoxes2(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)

        capacity.sort(reverse=True)

        count = 0
        for cap in capacity:
            if total_apples <= 0:
                break
            total_apples -= cap
            count += 1

        return count


apple = [1, 8, 6, 8, 9, 3, 3]
capacity = [10, 6, 8, 7, 3, 6]
sol = Solution()
print(sol.minimumBoxes2(apple, capacity))
