#暴力法 时间复杂度n
class Solution:
    def GetNumberOfK(self , data: List[int], k: int) -> int:
        # write code here
        count=0
        for i in range(len(data)):
            if data[i]==k:
                count=count+1
            elif data[i]>k:
                break
        return count
#时间复杂度O(n)
class Solution:
    def GetNumberOfK(self , data: List[int], k: int) -> int:
        # write code here
        if not data:
            return 0
        length=len(data)
        left=0
        right=length-1
        while (data[left]<k) and left<length-1:
            left+=1
        while (data[right]>k) and right>0:
            right-=1
        if left<=right and data[right]==k:
            return right-left+1
        else:
            return 0
#二分法查找O(log2n) 查找一半的数就能找到2的x次方等于n
#第一个大于等于k的位置(lower_bound)和第一个大于k的位置(upper_bound)，然后相减就可以得到答案了。

class Solution:
    def GetNumberOfK(self , data: List[int], k: int) -> int:
        # write code here
        return self.upper_bound(k,data)-self.lower_bound(k,data)
    # 下届，指向第一个目标值
    def lower_bound(self,k,data):
        left=0
        right=len(data)
        while left<right:
            mid=(left+right)//2
            if data[mid]>=k:
                right=mid
            else:
                left=mid+1
        return left

    # 上届，指向大于目标的第一个值 考虑值不存在的情况
    def upper_bound(self,k,data):
        left=0
        right=len(data)
        while left<right:
            mid=(left+right)//2
            if data[mid]>k:
                right=mid
            else:
                left=mid+1
        return right
class Solution:
    def __init__(self):
        self.count=0
    def GetNumberOfK(self , data: List[int], k: int) -> int:
        # write code here
        if not data:
            return 0
        if data[len(data)//2]<k:
            self.GetNumberOfK(data[len(data)//2+1:], k)
        elif data[len(data)//2]>k:
            self.GetNumberOfK(data[0:len(data)//2], k)
        else:
            self.count+=1
            self.GetNumberOfK(data[0:len(data)//2], k) and self.GetNumberOfK(data[len(data)//2+1:], k)
        return self.count