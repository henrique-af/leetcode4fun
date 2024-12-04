class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        l1, l2 = len(str1), len(str2)
        if l1 < l2:
            return False

        it1, it2 = 0, 0

        while it1 < l1 and it2 < l2:
            next_char = 'a' if str1[it1] == 'z' else chr(ord(str1[it1]) + 1)
            if str1[it1] == str2[it2] or next_char == str2[it2]:
                it2 += 1
            it1 += 1

        return it2 == l2