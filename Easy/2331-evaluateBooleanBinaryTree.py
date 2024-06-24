from typing import Optional, Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        stack = [root]
        res: Dict[TreeNode, int] = {} 

        while stack:
            last_node = stack[-1] 
            if not last_node.left and not last_node.right:  
                stack.pop() 
                res[last_node] = last_node.val

            elif (
                last_node.left in res and last_node.right in res
            ):  
                stack.pop()  
                if last_node.val == 2: 
                    res[last_node] = res[last_node.left] or res[last_node.right]
                elif last_node.val == 3: 
                    res[last_node] = res[last_node.left] and res[last_node.right]
            elif (
                last_node.left and last_node.right
            ):  
                if (
                    last_node.right not in res
                ):  
                    stack.append(last_node.right)
                if (
                    last_node.left not in res
                ):  
                    stack.append(last_node.left)

        return bool(res[root]) 



if __name__ == "__main__":
    # Constructing the tree:
    #        3
    #       / \
    #      2   2
    #     / \ / \
    #    0  1 0  1
    node0_1 = TreeNode(0)
    node1_1 = TreeNode(1)
    node0_2 = TreeNode(0)
    node1_2 = TreeNode(1)
    node2_1 = TreeNode(2, node0_1, node1_1)
    node2_2 = TreeNode(2, node0_2, node1_2)
    root = TreeNode(3, node2_1, node2_2)

    sol = Solution()
    result = sol.evaluateTree(root)
    print(result) 
