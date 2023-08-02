class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.root = 0

    def FindPath(self, root: TreeNode, sum: int) -> int:
        # write code here
        if not root:
            return 0
        self.FindSum(root, sum)
        self.FindPath(root.left, sum)
        self.FindPath(root.right, sum)
        return self.root

    def FindSum(self, root, sum):
        if not root:
            return 0
        d = []
        d.append(root)
        while (len(d)):
            for i in range(len(d)):
                r = d.pop()
                if sum == root.val:
                    self.root = self.root + 1
                if r.left:
                    self.FindSum(root.left, sum - root.val)
                if r.right:
                    self.FindSum(root.right, sum - root.val)