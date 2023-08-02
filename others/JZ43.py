#整数中1出现的次数
#法1，暴力法
class Solution:
    def NumberOf1Between1AndN_Solution(self , n: int) -> int:
        # write code here
        res=0
        while n>0:
            res+=self.number(n)
            n=n-1
        return res
    def number(self,n):
        res=0
        while n>0:
            l=n%10
            if l==1:
                res+=1
            n=n//10
        return res
#暴力2 调库
class Solution2:
    def NumberOf1Between1AndN_Solution(self , n: int) -> int:
        # write code here
        res = 0
        for i in range(1, n + 1):
            tmp_str = str(i)
            res += tmp_str.count('1')
        return res
