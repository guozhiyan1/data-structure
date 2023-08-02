'''
判断是不是平衡二叉树：此处不管是否是二叉搜索树，只关心任何一个结点两个子树高度差都不能超过1
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self , pRoot: TreeNode) -> bool:
        if not pRoot:
            return True
        left=self.depth(pRoot.left)
        right=self.depth(pRoot.right)
        if abs(left-right)>1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    def depth(self,root):
        if not root:
            return 0
        left=self.depth(root.left)
        right = self.depth(root.right)
        return max([left,right])+1