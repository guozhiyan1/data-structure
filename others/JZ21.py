#调整数组顺序使奇数位于偶数前面(一) 双指针
class Solution:
    def reOrderArray(self , array: List[int]) -> List[int]:
        # write code here
        odd=0
        for i in range(len(array)):
            if array[i]%2!=0:
                odd+=1
        b=[1 for _ in range(len(array))]
        j=0
        for i in range(len(array)):
            if array[i]%2==1:
                b[j]=array[i]
                j+=1
            else:
                b[odd]=array[i]
                odd+=1
        return b