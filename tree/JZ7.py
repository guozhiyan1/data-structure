class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可

# @param pre int整型一维数组
# @param vin int整型一维数组
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self , pre: List[int], vin: List[int]) -> TreeNode:
        # write code here
        l=len(pre)
        if l==0:
            return None
        elif l==1:
            return TreeNode(pre[0])
        else:
            root=TreeNode(pre[0])
            i=vin.index(pre[0])
            root.left=self.reConstructBinaryTree(pre[1:1+i], vin[0:i])
            root.right=self.reConstructBinaryTree(pre[1+i:], vin[1+i:])
        return root