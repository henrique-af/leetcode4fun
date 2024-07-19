from typing import List, Optional


# Definição da classe TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while i < len(values):
        current = queue.pop(0)

        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        if not root:
            return []

        to_delete_set = set(to_delete)
        res = []

        def dfs(node: Optional[TreeNode], is_root: bool) -> Optional[TreeNode]:
            if not node:
                return None

            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                res.append(node)

            node.left = dfs(node.left, root_deleted)
            node.right = dfs(node.right, root_deleted)

            return None if root_deleted else node

        dfs(root, True)
        return res


def printTree(root: TreeNode, level=0, label="."):
    prefix = " " * (level * 4)
    print(prefix + label + ": ", root.val if root else None)
    if root:
        if root.left or root.right:
            if root.left:
                printTree(root.left, level + 1, "L")
            else:
                print(prefix + "    L: None")
            if root.right:
                printTree(root.right, level + 1, "R")
            else:
                print(prefix + "    R: None")


values = [1, 2, 3, 4, 5, 6, 7]
root = buildTree(values)

to_delete = [3, 5]
sol = Solution()
forest = sol.delNodes(root, to_delete)

for tree in forest:
    printTree(tree)
    print("------")
