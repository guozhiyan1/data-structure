
"""从第二个元素开始和前面的元素进行比较，如果前面的元素比当前元素大，则将前面元素后移，当前元素依次往前，
直到找到比它小或等于它的元素插入在其后面，然后选择第三个元素，重复上述操作，进行插入，依次选择到最后一个元素，插入后即完成所有排序
[10,7,3,9,8,1,4,5]
i=1 1位和0位比较   7比10小 放在10前面  [7.10]
i=2 2位和0、1位比较

i=7 7位和0~6位比较
时间复杂度O(n^2)， 空间复杂度O(1)
"""
class Solution:
    def InsertSort(self,nums):
        length=len(nums)
        for i in range(1,length):
            for j in range(0,i):
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums
if __name__ == '__main__':
    a=Solution()
    nums=[10,7,3,9,8,1,4,5]
    print(a.InsertSort(nums))


