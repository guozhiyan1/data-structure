class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Mirror(self , pRoot: TreeNode) -> TreeNode:
        # write code here
        if pRoot==None:
            return pRoot
        pRoot1=TreeNode(pRoot.val)
        pRoot1.left=self.Mirror(pRoot.right)
        pRoot1.right=self.Mirror(pRoot.left)
        return pRoot1