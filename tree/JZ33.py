'''二叉搜索数的后序遍历
二叉搜索树指数的左节点都小于根结点，右节点都大于根节点
基于后序遍历为左节点--右节点--根节点，所以根节点是最后一个。比根节点小的为左节点，大的为右节点.讲左右结点依次迭代。判断所有结点
[1,3,2,8]  0,3  要么都小
[10,8]   true
[10,9,   8]  true   要么都大
[5,7,6,    9,11,10,8]  一边大 一遍小

这题做了我一天，辛苦辛苦
'''
class Solution:
    def VerifySquenceOfBST(self , sequence: List[int]) -> bool:
        # write code here
        if not sequence:
            return False
        length=len(sequence)
        root=sequence[-1]
        if length==1:
            return True
        for i in range(length-1):
            if length>1:
                left_max = max(sequence[:i+1])
                right_min=min(sequence[i+1:length-1]) if i<length-2 else root
                if left_max<root<right_min:
                    return self.VerifySquenceOfBST(sequence[0:i+1]) and self.VerifySquenceOfBST(sequence[i+1:length-1])
                elif root==right_min:
                    return self.VerifySquenceOfBST(sequence[0:length-1])
                if sequence[i]>root and sequence[i+1]<root:
                    return False
class Solution1:
    def VerifySquenceOfBST(self , sequence: List[int]) -> bool:
        # write code here
        length=len(sequence)
        if not sequence:
            return False
        if length==1:
            return True
        l1=0
        l2=0
        for i in range(length-1):
            if sequence[i]<sequence[length-1]:
                l1=l1+1
            if sequence[i]>sequence[length-1]:
                    l2=l2+1
        if length-l1<=1:
            return self.VerifySquenceOfBST(sequence[0:l1])
        if length-l2<=1:
            return self.VerifySquenceOfBST(sequence[0:l2])
        for i in range(l1):
            if sequence[i]>sequence[length-1]:
                return False
        for i in range(l1,l1+l2-1):
            if sequence[i]<sequence[length-1]:
                return False
        return self.VerifySquenceOfBST(sequence[0:l1]) and self.VerifySquenceOfBST(sequence[l1:l1+l2])