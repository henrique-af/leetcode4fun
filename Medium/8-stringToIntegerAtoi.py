class Solution:
    def myAtoi(self, s: str) -> int:
        min_int = -(2**31)
        max_int = 2**31 - 1
        c = 0

        while c < len(s) and s[c] == " ":
            c += 1  

        sign = 1
        if c < len(s) and (s[c] == "+" or s[c] == "-"):
            sign = 1 if s[c] == "+" else -1
            c += 1  
        
        num = 0
        while c < len(s) and s[c].isdigit():  
            digit = int(s[c])
            if num > (max_int - digit) // 10: 
                return max_int if sign == 1 else min_int
            num = num * 10 + digit
            c += 1 

        return num * sign

sol = Solution()
print(sol.myAtoi("wwwwwwww -42"))
