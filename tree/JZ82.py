#二叉树中和为某一值的路径是否存在
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        # write code here
        if not root:
            return False
        d=[]
        d.append(root)
        while(len(d)!=0):
            for i in range(len(d)):
                r=d.pop()
                if r.left is not None or r.right is not None:
                    return self.hasPathSum(r.left, sum-r.val) or self.hasPathSum(r.right, sum-r.val)
                else:
                    if sum==r.val:return True
                    if sum!=r.val:return False