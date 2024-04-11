def removeKdigits(num, k):
    result = []
    for digit in num:
        while k > 0 and result and result[-1] > digit:
            result.pop()
            k -= 1
        result.append(digit)
    final_result = result[:-k] if k else result
    return ''.join(final_result).lstrip('0') or '0'

num = "1432219"
k = 3
print(removeKdigits(num, k))
