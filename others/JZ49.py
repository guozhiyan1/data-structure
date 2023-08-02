"""
把只包含质因子2、3和5的数称作丑数
首先除2，直到不能整除为止，然后除5到不能整除为止，然后除3直到不能整除为止。最终判断剩余的数字是否为1，如果是1则为丑数，否则不是丑数
前20个丑数为：1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36
求按从小到大的顺序的第 n个丑数
"""
#法一：递归
import sys
sys.setrecursionlimit(1000000)
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 1:
            return 1
        n = self.GetUglyNumber_Solution(index - 1) + 1
        a = n
        while (self.loop(a) != 1):
            n += 1
            a = n
            self.loop(a)
        else:
            return n

    def loop(self, a):
        while a % 2 == 0:
            a = a / 2
        while a % 3 == 0:
            a = a / 3
        while a % 5 == 0:
            a = a / 5
        return a
    #法二 动态规划
"""首先从丑数的定义我们知道，一个丑数的因子只有2,3,5，那么丑数p = 2 ^ x * 3 ^ y * 5 ^ z
换句话说一个丑数一定由另一个丑数乘以2或者乘以3或者乘以5得到或者说一个丑数乘以2or3or5一定会是另外一个丑数
所以我们采用另外一种方法，设顺序排列的N个丑数的数组为result[N]
首先从最小的丑数:reslut[1]=1开始.分别乘2，3，5得到三个数，然后选择最小的数2放入result[2] = 2
1）丑数数组： 1
乘以2的队列：2
乘以3的队列：3
乘以5的队列：5
丑数数组有1,2时，
2）丑数数组：1,2。择最小的数3放入result[3] = 3
乘以2的队列：  4
乘以3的队列：3，6
乘以5的队列：5，10，
2）丑数数组：1,2，3。择最小的数3放入result[3] = 4
乘以2的队列：   4
乘以3的队列：   6
乘以5的队列：5，10
"""
class Solution:
        def GetUglyNumber_Solution(self, index):
            # 排除0
            if index == 0:
                return 0
            # 按顺序记录丑数
            num = []
            num.append(1)
            # 记录这是第几个丑数
            count = 1;
            # 分别代表要乘上2 3 5的下标
            i = 0
            j = 0
            k = 0
            while count < index:
                # 找到三个数中最小的丑数
                num.append(min(num[i] * 2, min(num[j] * 3, num[k] * 5)));
                count += 1
                # 由2与已知丑数相乘得到的丑数，那该下标及之前的在2这里都用不上了
                if num[count - 1] == num[i] * 2:
                    i += 1
                # 由3与已知丑数相乘得到的丑数，那该下标及之前的在3这里都用不上了
                if num[count - 1] == num[j] * 3:
                    j += 1
                    # 由5与已知丑数相乘得到的丑数，那该下标及之前的在5这里都用不上了
                if num[count - 1] == num[k] * 5:
                    k += 1
            return num[count - 1]


