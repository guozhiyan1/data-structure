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
#法2：双指针

#法3：双端队列
'''输入: nums = [1,2,3,4] 和 k = 3  l-(size-1)=2个数
输出: [3,4]
解释:
1.i=0,quene=0   
2.i=1，nums[1]>num[0]    quene移除0加入1             
3.i=2，  num[2]>num[1]  quene移除1加入2    且2>=2     res追加num[2]=3                 
  i=3，  num[3]>num[2]   quene移除2加入3   且3>=2      res追加num[3]=4 
输入[2,3,4,2,6,2,5,1],3    l-(size-1)=6个数
i=0    quene=0
i=1    num[1]>num[0]  quene=1
i=2    num[2]>num[1]  quene=2               i>=2:res=num[2]=[4]
i=3    num[3]<num[2]  quene=[2,3]           i>=2:res=[num[2]]=[4]
i=4    num[4]>num[3]  quene=[4]           i>=2:res=[num[4]]=[6]
i=5  5-2>2 quene=[4]  num[5]<num[4] quene=[4,5] i>=2 res=[num[4]]=6
i=6   
i=7
'''
class Solution1:
    def maxInWindows(self , num, size):
        if not num or size==0:
            return []
        quene=[]
        res=[]
        for i in range(len(num)):
            if len(quene)>0:
                if(i-quene[0])>(size-1):
                    quene.pop(0)
                while len(quene)>0 and num[i]>=num[quene[-1]]:
                    quene.pop(-1)
            quene.append(i)
            if i>=size-1:
                res.append(num[quene[0]])
        return res



