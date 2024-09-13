class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_result = start ^ goal
        bit_flips = bin(xor_result).count('1')

        return bit_flips
