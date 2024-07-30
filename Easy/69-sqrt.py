class Solution:

    def mySqrt(self, x: int,tolerance=1e-10) -> int:
        if x < 0:
            raise ValueError("Cannot compute the square root of a negative number")
        if x == 0:
            return 0

        x = x
        while True:
            root = 0.5 * (x + (x / x))
            if abs(root - x) < tolerance:
                return root
            x = root



sol = Solution()
sol.mySqrt(4)
