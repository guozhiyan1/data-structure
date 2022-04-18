#滑动窗口的最大值
#法一暴力法
class Solution:
    def maxInWindows(self , num: List[int], size: int) -> List[int]:
        # write code here
        l=len(num)
        if size>l:
            return None
        if size<=0:
            return None
        result=[]
        for i in range(l-(size-1)):
            list=[]
            for j in range(size):
                list.append(num[j+i])
            result.append(max(list))
        return result
#法一优化
class Solution:
    def maxInWindows(self , num: List[int], size: int) -> List[int]:
        # write code here
        l=len(num)
        if size>l or size<=0:
            return None
        result=[]
        for i in range(l-(size-1)):
            a=max(num[i:i+size])
            result.append(a)
        return result
#法2：双端队列
'''[2,3,4,2,6,2,5,1] size=3
i=0   quene=[2]
i=1   quene=[3]  2<3   删除2
i=2   quene=[4]  3<4   删除3

i=7
'''
class Solution1:
    def maxInWindows(self , num: List[int], size: int) -> List[int]:
        quene=[]
        res=[]
        i=0
        while size>0 and i<len(num):
            if len(quene)>0 and i-size+1>quene[0]:
                quene.pop(0)
            while len(quene)>0 and num[quene[-1]]<num[i]:
                quene.pop()
            quene.append(i)
            if i>=size-1:
                res.append(num[quene[0]])
            i=i+1
        return res

'''输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
滑动窗口的位置 最大值
[1 3 -1] -3 5 3 6 7 3
1 [3 -1 -3] 5 3 6 7 3
1 3 [-1 -3 5] 3 6 7 5
1 3 -1 [-3 5 3] 6 7 5
1 3 -1 -3 [5 3 6] 7 6
1 3 -1 -3 5 [3 6 7] 7

'''