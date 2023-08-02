class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self , root: TreeNode, p: int, q: int) -> int:
        # write code here
        if not root:
            return None
        if root.val==p or root.val==q:
            return root.val
        if p>root.val>q or p<root.val<q:
            return root.val
        elif p<root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p>root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return None