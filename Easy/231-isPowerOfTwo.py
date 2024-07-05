import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        log_n_base_2 = math.log2(n)
        return log_n_base_2.is_integer()
