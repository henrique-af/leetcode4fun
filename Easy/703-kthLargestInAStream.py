import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

commands = ["KthLargest", "add", "add", "add", "add", "add"]
inputs = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

output = []

# Execute the commands
for command, input in zip(commands, inputs):
    if command == "KthLargest":
        k, nums = input
        obj = KthLargest(k, nums)
        output.append(None)
    elif command == "add":
        val = input[0]
        result = obj.add(val)
        output.append(result)

print(output) 
