class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        bit_mask = 0
        for c in allowed:
            bit = 1 << (ord(c) - ord('a'))
            bit_mask |= bit 
        
        consistent_count = 0
        for w in words:
            consistent = True
            for c in w:
                bit = 1 << (ord(c) - ord('a'))
                if bit & bit_mask == 0:
                    consistent = False
                    break
            if consistent:
                consistent_count += 1
        
        return consistent_count