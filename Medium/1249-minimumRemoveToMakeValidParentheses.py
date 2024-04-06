class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        s_list = list(s)

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)

        to_remove.update(stack)

        result = ''.join([s_list[i] for i in range(len(s_list)) if i not in to_remove])

        return result

sol = Solution()
print(sol.minRemoveToMakeValid("lee(t(c)o)de)")) 
