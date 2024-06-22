from typing import List


def SlidingWindow(arr: List[int], k: int) -> int:
    n = len(arr)

    if n < k:
        return -1

    current_sum = sum(arr[:k])
    max_sum = current_sum

    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


arr = [1, 3, 2, 5, 7, 2]
k = 3
result = SlidingWindow(arr, k)
print(result)
