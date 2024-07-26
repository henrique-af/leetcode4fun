class Solution:
    def __init__(self):
        self.xmin = -5 * 10**4
        self.bucket = [[] for _ in range(64)]

    def radix_sort(self, nums):
        # 1st round
        for x in nums:
            x -= self.xmin
            self.bucket[x & 63].append(x)

        i = 0
        for B in self.bucket:
            for v in B:
                nums[i] = v
                i += 1
            B.clear()

        # 2nd round
        for x in nums:
            self.bucket[(x >> 6) & 63].append(x)

        i = 0
        for B in self.bucket:
            for v in B:
                nums[i] = v
                i += 1
            B.clear()

        # 3rd round
        for x in nums:
            self.bucket[x >> 12].append(x)

        i = 0
        for B in self.bucket:
            for v in B:
                nums[i] = v + self.xmin
                i += 1

    def sortArray(self, nums):
        self.radix_sort(nums)
        return nums


nums = [5, 2, 3, 1]
sol = Solution()
print(sol.sortArray(nums))
