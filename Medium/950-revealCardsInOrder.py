from collections import deque
from typing import List



class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        result = [0] * n
        indices = deque(range(n))

        for card in deck:
            index = indices.popleft()
            result[index] = card
            if indices:
                indices.append(indices.popleft())
        return result

deck = [17,13,11,2,3,5,7]
sol = Solution()
sol.deckRevealedIncreasing(deck)