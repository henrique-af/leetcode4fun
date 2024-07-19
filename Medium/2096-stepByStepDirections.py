class Solution:
    def findLCA(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.findLCA(root.left, p, q)
        right = self.findLCA(root.right, p, q)
        if left and right:
            return root
        return left if left else right

    def findPath(self, root, value, path):
        if not root:
            return False
        if root.val == value:
            return True
        path.append("L")
        if self.findPath(root.left, value, path):
            return True
        path.pop()
        path.append("R")
        if self.findPath(root.right, value, path):
            return True
        path.pop()
        return False

    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        def findNode(root, value):
            if not root:
                return None
            if root.val == value:
                return root
            left = findNode(root.left, value)
            if left:
                return left
            return findNode(root.right, value)

        startNode = findNode(root, startValue)
        destNode = findNode(root, destValue)

        lca = self.findLCA(root, startNode, destNode)

        pathToStart = []
        self.findPath(lca, startValue, pathToStart)

        pathToDest = []
        self.findPath(lca, destValue, pathToDest)

        pathToStart = ["U"] * len(pathToStart)
        finalPath = "".join(pathToStart + pathToDest)
        return finalPath
