# 和为S的两个数字 输入一个升序数组 array 和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，返回任意一组即可，如果无法找出这样的数字，返回一个空数组即可
#法一 暴力法
class Solution:
    def FindNumbersWithSum(self , array, sum: int):
        # write code here
        a=[]
        for i in range(len(array)):
            for j in range(i+1,len(array)):
                if array[i]+array[j]==sum:
                    a.append(array[i])
                    a.append(array[j])
                    return a
        return None
#法二 哈希法
class Solution1:
    def FindNumbersWithSum(self , array , sum):
        # write code here
        d={}
        a=[]
        for i in range(len(array)):
            if sum-array[i] not in d:
                d[array[i]]=i
            else:
                a.append(array[i])
                a.append(sum-array[i])
                return a
        return None
# 法三 双指针
"""step 1：准备左右双指针分别指向数组首尾元素。
step 2：如果两个指针下的和正好等于目标值sum，则找到了所求的两个元素。
step 3：如果两个指针下的和大于目标值sum，右指针左移；如果两个指针下的和小于目标值sum，左指针右移。
step 4：当两指针对撞时，还没有找到，就是数组没有。
[1,2,4,7,11,15],15

"""
class Solution3:
    def FindNumbersWithSum(self , array, sum):
        # write code here
        length=len(array)
        l=0
        r=length-1
        res=[]
        while l<r:
            sum1=array[l]+array[r]
            if sum1==sum:
                res.append(array[l])
                res.append(array[r])
                return res
            elif sum1>sum:
                r-=1
            elif sum1<sum:
                l+=1
        return None
#法四:二分查找 递增数组  [1,2,4,7,11,15],13
"""
假设当前值为arr[i], 那么第二个数为sum-arr[i]。
sum-arr[i] 与 arr[i]的大小分为三种情况：
a. 如果sum-arr[i] arr[i]相等，那么只需要查找i两侧的值；
b. 如果sum-arr[i]小于arr[i]，那么在i 的左侧查找sum-arr[i];
c. 如果sum-arr[i]大于arr[i], 那么在i 的右测查找sum-arr[i];
"""