from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inTraverse(self, root: Optional[TreeNode], inorder: List[int]):
        if not root:
            return
        self.inTraverse(root.left, inorder)
        inorder.append(root.val)
        self.inTraverse(root.right, inorder)

    def constructBalancedBST(
        self, inorder: List[int], low: int, high: int
    ) -> Optional[TreeNode]:
        if low > high:
            return None

        mid = low + (high - low) // 2
        curr = TreeNode(inorder[mid])
        curr.left = self.constructBalancedBST(inorder, low, mid - 1)
        curr.right = self.constructBalancedBST(inorder, mid + 1, high)
        return curr

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        inorder = []
        self.inTraverse(root, inorder)
        return self.constructBalancedBST(inorder, 0, len(inorder) - 1)

root = [1, null, 2, null, 3, null, 4, null, null]
sol = Solution()
sol.balanceBST(root)