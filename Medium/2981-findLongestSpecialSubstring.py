class Solution:
    def maximumLength(self, s: str) -> int:
        def is_valid(length):
            # Check if there's a special substring of given length occurring at least 3 times
            count_map = {}
            for i in range(len(s) - length + 1):
                substring = s[i:i+length]
                if len(set(substring)) == 1:  # Check if all characters are the same
                    count_map[substring] = count_map.get(substring, 0) + 1
                    if count_map[substring] >= 3:
                        return True
            return False

        # Binary search for maximum length
        l, r = 1, len(s)
        result = -1
        while l <= r:
            mid = (l + r) // 2
            if is_valid(mid):
                result = mid
                l = mid + 1
            else:
                r = mid - 1

        return result
    
sol = Solution()
sol.maximumLength("aaaa")