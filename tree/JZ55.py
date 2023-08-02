#二叉树的深度
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归的方法求深度，深度是根结点到叶子结点的最大路径+1
class Solution1:
    def TreeDepth(self , pRoot: TreeNode):
        if not pRoot:
            return 0
        left=right=0
        if pRoot.left:
            left=self.TreeDepth(pRoot.left)
        if pRoot.right:
            right=self.TreeDepth(pRoot.right)
        return max([left,right])+1
#广度遍历，即层次遍历
class Solution2:
    def TreeDepth(self , pRoot: TreeNode):
        if not pRoot:
            return 0
        d=[]
        d.append(pRoot)
        depth=0
        while(len(d)!=0):
            for i in range(len(d)):
                r=d.pop(0)
                if r.left is not None:
                    d.append(r.left)
                if r.right is not None:
                    d.append(r.right)
            depth=depth+1
        return depth