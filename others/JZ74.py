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
"""
class Solution1:
    def FindContinuousSequence(self , sum):
        res = []
        #从1到2的区间开始
        l = 1
        r = 2
        while l < r:
            #计算区间内的连续和
            sum1 = (l + r) * (r - l + 1) / 2
            #如果区间内和等于目标数
            if sum1 == sum:
                temp = []
                #记录区间序列
                for i in range(l, r + 1):
                    temp.append(i)
                res.append(temp)
                #左区间向右
                l += 1
            #如果区间内的序列和小于目标数，右区间扩展
            elif sum1 < sum:
                r += 1
            #如果区间内的序列和大于目标数，左区间收缩
            else:
                l += 1
        return res
