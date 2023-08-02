#暴露解法，会超时
class Solution:
    def MoreThanHalfNum_Solution(self , numbers):
        # write code here
        length=len(numbers)
        for i in range(length):
            if numbers.count(numbers[i])<=length//2:
                continue
            else:
                return numbers[i]
#法二 哈希法
class Solution:
    def MoreThanHalfNum_Solution(self , numbers: List[int]) -> int:
        # write code here
        length=len(numbers)
        if length==1:
            return numbers[0]
        n=length//2
        a={}
        b={}
        c=2
        for i in range(length):
            if numbers[i] not in a.values():
                a[i]=numbers[i]
            else:
                if numbers[i] in b.keys():
                    b[numbers[i]]+=1
                else:
                    b[numbers[i]]=2
        for i in b:
            if b[i]>n:
                return i
#法三 只需要把数组升序或降序排列胡来，中间位置对应的值（众数）就是要找的数字
class Solution:
    def MoreThanHalfNum_Solution(self , numbers: List[int]) -> int:
        # write code here
        if numbers == []:
            return None
        #对数组排序
        numbers.sort()
        #返回中间位置所在数字即所求
        return numbers[len(numbers)//2]
"""摩尔投票算法
一下摩尔投票算法的一些基础知识。

概念：指通过线性的时间和固定的空间来找到一组序列中众数是哪一个的一种算法。
具体步骤：
首先创建一个初始指针，从序列一开始位置扫描；同时这个指针扫描的对象包含： a current candidate（一个当前的候选人）和a counter（当前候选人的票数）。当然一开始这个候选人是未知的；票数也就是0。
接着移动指针经过每个元素：
如果一开始的票数为0，那么就把当前元素作为candidate，并且票数变为1；
如果票数不为0，那么就根据该元素是否与candidate相同，相同则票数＋1；否则票数减1。 当票数减为0 后，又开始寻找新的candidate并统计票数，重复前面的步骤。
直到指针走完整个序列，如果序列存在众数，那么当前的candidate就是我们要找的众数。
接下来看本题，本题要找数组中出现次数超过一半的数字，且题目告诉我们👉给定的数组总是存在多数元素👈其实是变相告诉我们，“众数”是存在于这个数组中的！ 所以这里我们也可以采用摩尔投票算法的思路来解，下面看本题摩尔算法的图解示例1：

出现次数超过一半可以跟数组中其他元素抵消后还会剩下来
遍历数组，候选票数为0，记录一个候选元素，遇到相同元素候选票数累加，不同元素则自减

[1,2,3,2,2,2,5,4,2]
i=1   候选人=1  票数=1
i=2   候选人=1  票数=0
i=3   候选人=3  票数=1
i=2   候选人=3  票数=0
i=2   候选人=2  票数=1
i=2   候选人=2  票数=2
i=5   候选人=2  票数=1
i=4   候选人=2  票数=0
i=2   候选人=2  票数=1
"""
# -*- coding:utf-8 -*-

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        counts = 0             #定义初始票数为0
        candidate = None       #初始候选人为None
        for i in numbers:      #接下来利用摩尔投票遍历数组
            if counts == 0:     #首先初始元素就是当前候选人，所以票数自然+1
                candidate = i
            counts += (1 if i == candidate else -1)  #接下来比较候选人是否相同，相同候选人就+1；不同就-1
        return candidate