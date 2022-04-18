#旋转数组的最小数字
'''
[1,2,3,4,5]
[3,4,5,1,2] [4,5,1,2] [5,1,2,3,4] [2,3,4,5]
二分查找难就难在，arr[mid]跟谁比.
我们的目的是：当进行一次比较时，一定能够确定答案在mid的某一侧。一次比较为 arr[mid]跟谁比的问题。
一般的比较原则有：

如果有目标值target，那么直接让arr[mid] 和 target 比较即可。
如果没有目标值，一般可以考虑 端点
那我们肯定在想，能不能把左端点看成target， 答案是不能。
原因：
情况1 ：1 2 3 4 5 ， arr[mid] = 3. target = 1, arr[mid] > target, 答案在mid 的左侧
情况2 ：3 4 5 1 2 ， arr[mid] = 5, target = 3, arr[mid] > target, 答案却在mid 的右侧
所以不能把左端点当做target
把右端点看作taget
[3,4,5,1,2] arr[mid] = 5,   如果5比2大，看右边[mid+1],right
[5,1,2，3，4] arr[mid] = 2,如果2比4小，看左边
'''
class Solution:
    def minNumberInRotateArray(self , rotateArray: List[int]) -> int:
        # write code here
        length=len(rotateArray)
        mid=length//2
        left=0
        right=length-1
        while left<right:
            mid=(left+right)//2
            if rotateArray[mid]>=rotateArray[right]:
                left=mid+1
            else:
                right=mid-1
        return rotateArray[left]