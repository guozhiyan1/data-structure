#调整数组顺序使奇数位于偶数前面(一) 双指针
"""
step 1：遍历数组，统计奇数出现的次数，即找到了偶数开始的位置。
step 2：准备一个和原数组同样长的新数组承接输出，准备双指针，x指向奇数开始的位置，y指向偶数开始的位置。
step 3：遍历原数组，遇到奇数添加在指针x后面，遇到偶数添加在指针y后面，直到遍历结束。
"""
class Solution:
    def reOrderArray(self , array):
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
"""
逐个判断，偶数的话，后面的奇数放他前面
"""
class Solution1:
    def reOrderArray(self , array: List[int]) -> List[int]:
        # write code here
        if not array:
            return None
        for i in range(len(array)):
            if array[i]%2==1:
                continue
            else:
                for j in range(i+1,len(array)):
                    if array[j]%2==0:
                        continue
                    else:
                        k=array.pop(j)
                        array.insert(i,k)
                        break
        return array