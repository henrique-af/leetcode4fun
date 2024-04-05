def isPalindrome(x):
    x_str = str(x)
    if x < 0:
        return False
    x_list = list(map(int, x_str))
    count = len(x_list) - 1
    x_reversed = []
    for i in range(len(x_list)):
        x_reversed.append(x_list[count])
        count -= 1
    return x_list == x_reversed


x = -121
print(isPalindrome(x)) 