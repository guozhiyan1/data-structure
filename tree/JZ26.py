#树的子结构
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''空树不是任意一个树的子结构，如果 root1 与root2 中有一个为空树的话，返回False
当rootA的值与rootB一致时，B是A的子结构（且A的左子树等于B左子树，A的右子树等于B右子树）
当A的左子树等于B，B是A的子结构
当A的右子树等于B，B是A的子结构
左右子树判断的时候，由于左子树还有左子树 所以可以接着本函数递归
'''


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot2 or not pRoot1:
            return False
        return self.IsSub(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
        # 判断两个树是否一致
        def IsSub(self, pRoot1, pRoot2):
            if not pRoot2:
                return True
            if not pRoot1:
                return False
            return pRoot1.val == pRoot2.val and self.IsSub(pRoot1.left, pRoot2.left) and self.IsSub(pRoot1.right,pRoot2.right)
