# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree_from_list(values):
    if not values:
        return None
    nodes = [TreeNode(val=val) for val in values]
    for i in range(len(nodes)):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == (root.left.val + root.right.val):
            return True
        else:
            return False


root_list = [10,4,6]
root = create_tree_from_list(root_list)

sol = Solution()
print(sol.checkTree(root))
