class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self , root: TreeNode, o1: int, o2: int) -> int:
        # write code here
        if not root:
            return None
        if root.val==o1 or root.val==o2:
            return root.val
        left=self.lowestCommonAncestor(root.left, o1, o2)
        right=self.lowestCommonAncestor(root.right, o1, o2)
        if left is not None and right is not None:
            return root.val
        if left is None:
            return right
        if right is None:
            return left
        return None