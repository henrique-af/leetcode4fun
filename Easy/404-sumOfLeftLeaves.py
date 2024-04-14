from typing import Optional


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = 0

        if root.left:
            if not root.left.left and not root.left.right:
                ans += root.left.val
            else:
                ans += self.sumOfLeftLeaves(root.left)

        ans += self.sumOfLeftLeaves(root.right)

        return ans


root = [3,9,20,null,null,15,7]
sol = Solution()
print(sol.sumOfLeftLeaves(root))
