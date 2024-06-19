# dividing and conquering!
from typing import List
import numpy as np


def binarySearch(n:int, list: List[int]):
    l = 0
    r = len(list) - 1
    # need to find the number i want, using binary search and diving and coquering.

    while l <= r:
        m = (l + r) // 2
        if n > list[m]:
            l = m + 1
        elif n < list[m]:
            r = m - 1
        else:
            return f"Valor encontrado no index {m}!"
    else:
        return "Value not found"


list = np.random.randint(1000, size = 10010).tolist()
list.sort()
print(list)

number = 999
print(binarySearch(number, list))
