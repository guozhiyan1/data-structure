#连续子数组的最大和
class Solution:
    def FindGreatestSumOfSubArray(self , array: List[int]) -> int:
        # write code here
        length=len(array)
        sum=0
        ret=array[0]
        for i in range(length):      #长度扩展1位是[-1,-2,-3]最大是-1.不扩展会认为是0
            sum=max(array[i],sum+array[i])
            ret=max(ret,sum)
        return ret