# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs = 0

        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left_distance = dfs(node.left)
            right_distance = dfs(node.right)
            
            for d1 in left_distance:
                for d2 in right_distance:
                    if d1 + d2 <= distance:
                        self.pairs += 1

            sum_dist = left_distance + right_distance
            return [distance + 1 for distance in sum_dist]

        dfs(root)
        return self.pairs
