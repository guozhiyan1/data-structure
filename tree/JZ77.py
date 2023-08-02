# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# @param pRoot TreeNode类
# @return int整型二维数组
#法一：层次遍历BFS
class Solution:
    def Print(self , pRoot: TreeNode) -> List[List[int]]:
        # write code here
        if not pRoot:
            return None
        d=[]
        result=[]
        d.append(pRoot)
        depth=0
        while (len(d)!=0):
            depth=depth+1
            result1=[]
            for i in range(len(d)):
                r=d.pop(0)
                result1.append(r.val)
                if r.left is not None:
                    d.append(r.left)
                if r.right is not None:
                    d.append(r.right)
            if (depth%2==0):
                result1.reverse()
            result.append(result1)
        return result