'''二叉搜索数的后序遍历
二叉搜索树指数的左节点都小于根结点，右节点都大于根节点
基于后序遍历为左节点--右节点--根节点，所以根节点是最后一个。比根节点小的为左节点，大的为右节点
[1,3,2,8]  0,3  要么都小
[10,8]   true
[10,9,   8]  true   要么都大
[5,7,6,    9,11,10,8]  一边大 一遍小
'''
class Solution:
    def VerifySquenceOfBST(self , sequence: List[int]) -> bool:
        # write code here
        if not sequence:
            return False
        length=len(sequence)
        root=sequence[-1]
        count1=0
        count2=0
        if length==1:
            return True
        for i in range(length-1):
            if length>1:
                left_max = max(sequence[:i+1])
                right_min=min(sequence[i+1:length-1]) if i<length-2 else root
                if left_max<=root<right_min:
                    return self.VerifySquenceOfBST(sequence[0:i+1]) and self.VerifySquenceOfBST(sequence[i+1:length-1])
                elif root==right_min:
                    return self.VerifySquenceOfBST(sequence[0:length-1])
                if sequence[i]>root and sequence[i+1]<root:
                    return False