from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)
                result.append(node.val)
                inorder_traversal(node.right)

        inorder_traversal(root)
        return result
