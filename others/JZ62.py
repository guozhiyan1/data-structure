"""
孩子们的游戏(圆圈中最后剩下的数)
从0到n-1（首尾相接）中每次去掉第m个数，下一次从去掉数的下一个开始，直到剩下最后一个数
返回的是最后一个数
有数为0的特殊情况

一、某数取余多次与取一次相等，例如5%2=1，而5%2%2%2=1；二、取余运算满足结合律，例如a%n - 1=(a-1)%n (n > 1)；
"""
import sys
sys.setrecursionlimit(100000)
class Solution:
    def function(self, n: int, m: int) -> int:
        if n == 1:
            return 0
        #递归
        x = self.function(n - 1, m)
        #返回最后删除的那个元素
        return (m + x) % n

    def LastRemaining_Solution(self , n: int, m: int) -> int:
        #没有小朋友的情况
        if n == 0 or m == 0:
            return -1
        return self.function(n, m)
