def twoSum(nums, target):
    d = {}
    for index, i in enumerate(nums):
        if d.get(i) is not None:
            return[d.get(i), index]
        d[target-i] = index


nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))

#LeetCode 1
