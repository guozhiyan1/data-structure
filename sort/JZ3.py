#利用set集合，字典key不能重复，我之前傻了哈
class Solution:
    def duplicate(self , numbers):
        if not numbers:
            return -1
        d={}
        for num in numbers:
            if num not in d:
                d[num]=1
            else:
                return num
        return -1
class Solution1:
    def duplicate(self , numbers: List[int]) -> int:
        # write code here
        if not numbers:
            return -1
        length=len(numbers)
        for i in range(length):
            if numbers.count(numbers[i])!=1:
                return numbers[i]
        return -1
"""
法一：先排序，如果后面数字和前面相等的话就返回
"""
class Solution2:
    def duplicate(self , numbers):
        if not numbers:
            return -1
        numbers.sort()
        for i in range(len(numbers)):
            if numbers[i]==i:
                continue
            else:
                if numbers[i] == numbers[numbers[i]]:  #如果是[0,1,2,2]i=3,number[3]=number[2]     [0,1,4,4,4]i=2 number[2]=number[4] 长度为n的所有数字都在0~n-1完美匹配这个
                    return numbers[i]
        return -1
"""
数组中重复的数字
法一：排序
既然数组长度为nnn只包含了0到n−1n-1n−1的数字，那么如果数字没有重复，这些数字排序后将会与其下标一一对应。
那我们就可以考虑遍历数组，每次检查数字与下标是不是一致的，一致的说明它在属于它的位置上，不一致我们就将其交换到该数字作为下标的位置上，
如果交换过程中，那个位置已经出现了等于它下标的数字，那肯定就重复了。
[2,3,1,0,2,5,3] 7个小于7的数字
[0,1,2,2,3,3,5]  i=3 2==numbers[2]
"""
