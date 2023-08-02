#和为S的连续正数序列
"""法一
我们可以从数字1开始枚举连续的数字，将其累加判断其是否等于目标，如果小于目标数则继续往后累加，
如果大于目标数说明会超过，跳出，
继续枚举下一个数字开始的情况（比如2，比如3），这样每次都取连续的序列，只有刚好累加和等于目标数才可以记录从开始到结束这一串数字，代表是一个符合的序列
"""
class Solution:
    def FindContinuousSequence(self , sum: int):
        # write code here
        if not sum:
            return 0
        res=[]
        for i in range(1,sum):
            count=i
            a=[]
            a.append(i)
            for j in range(i+1,sum):
                count=count+j
                if count>sum:
                    break
                elif count==sum:
                    a.append(j)
                    res.append(a)
                else:
                    a.append(j)
        return res
"""法二：
从某一个数字开始的连续序列和等于目标数如果有，只能有一个，于是我们可以用这个性质来使区间滑动。
两个指针l、r指向区间首和区间尾，公式(l+r)/2∗(r−l+1)计算区间内部的序列和，如果这个和刚好等于目标数，说明以该区间首开始的序列找到了，记录下区间内的序列，同时以左边开始的起点就没有序列了，于是左区间收缩；如果区间和大于目标数，说明该区间过长需要收缩，只能收缩左边；如果该区间和小于目标数，说明该区间过短需要扩大，只能向右扩大，移动区间尾
1,2,3,4,5,6,7,8,9
l=1 r=2 小于9  移动右边界
l=1 r=4 大于9  10移动左边界 减1
l=2 r=4   符合
l=3 r=4        左边界移动 减2=7
l=3 r=5       有边界移动+5  大于9 移动左边界
l=4，r=5      等于9符合
l=5  r=6     大于9
l=6  r=7
l=7  r=8  
l=8 r=9
l=9   结束
"""
class Solution1:
    def FindContinuousSequence(self , sum: int) -> List[List[int]]:
        # write code here
        res=[]
        left,right=1,2
        while right<sum:
            count=(left+right)*(right-left+1)//2
            if count>sum:
                left+=1
            elif count<sum:
                right+=1
            else:
                res.append([i for i in range(left,right+1)])
                left+=1
        return res
