from typing import Counter, List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        available = Counter(hand)
        for card in sorted(available):
            count = available[card]
            if count == 0: continue
            for i in range(1, groupSize):
                if available[card+i] < count: return False
                available[card + i] -= count
            available[card] = 0
        return True
    
hand = [1]
groupSize = 1
sol = Solution()
print(sol.isNStraightHand(hand, groupSize))
