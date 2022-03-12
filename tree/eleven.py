'''二叉搜索树转换为排序的双向链表
二叉搜索树满足左子树的值<根结点的值<右子树的值，所以对二叉树进行中序遍历，然后对每个结点进行双向链接
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#中序遍历+数组
class Solution1:
    def Convert(self , pRootOfTree ):
        if not pRootOfTree:
            return None
        self.arr=[]
        #中序遍历self.arr是遍历好的值
        self.middle(pRootOfTree)
        for i in range(len(self.arr)-1):
            self.arr[i].right=self.arr[i+1]
            self.arr[i+1].left=self.arr[i]
        return self.arr[0]

    def middle(self,root):
        if not root:
            return None
        self.middle(root.left)
        self.arr.append(root)
        self.middle(root.right)

