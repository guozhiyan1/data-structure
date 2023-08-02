class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def KthNode(self , proot: TreeNode, k: int) -> int:
        # write code here
        a=self.preinorder(proot)
        if not a or len(a)<k or k<=0:
            return -1
        else:
            return a[k-1]
    def preinorder(self,proot):
        if not proot:
            return None
#         result=[]
        result1=[]
        d=[]
        d.append(proot)
        while (len(d)!=0):
            for _ in range(len(d)):
                r=d.pop(0)
                result1.append(r.val)
                if r.left:
                    d.append(r.left)
                if r.right:
                    d.append(r.right)
        result1.sort()
        return result1