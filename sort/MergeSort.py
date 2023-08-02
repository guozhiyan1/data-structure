"""
归并排序在于把序列拆分再合并起来，使用分治法来实现，这就意味这要构造递归算法
归并排序每次递归需要用到一个辅助表空间复杂度还是O(n),时间复杂度o(nlogn)
归并排序总时间=分解时间+子序列排好序时间+合并时间
分解时间是个常数
子序列排好序时间：规模为n的问题分成两个规模分别为n/2的子问题  时间复杂度是o（logn)
"""
class Solution:
    def MergeSort(self,nums):
        length=len(nums)
        if length<2:
            return nums
        mid=length//2
        s1=self.MergeSort(nums[0:mid])
        s2=self.MergeSort(nums[mid:])
        return self.Merge(s1,s2)
    def Merge(self,s1,s2):
        i=j=0
        a=[]
        while i<len(s1) and j<len(s2):
            if s1[i]<= s2[j]:
                a.append(s1[i])
                i += 1
            else:
                a.append(s2[j])
                j += 1
        a=a+s1[i:]+s2[j:]
        return a

if __name__ == '__main__':
    a = Solution()
    # nums=[10,7,3,9,8,1,4,5]
    nums=[3,7,5,1,4,2]
    print(a.MergeSort(nums))