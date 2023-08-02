#法一连续子数组的最大和
class Solution:
    def FindGreatestSumOfSubArray(self , array) -> int:
        # write code here
        length=len(array)
        sum=0
        ret=array[0]
        for i in range(length):      #长度扩展1位是[-1,-2,-3]最大是-1.不扩展会认为是0
            sum=max(array[i],sum+array[i])
            ret=max(ret,sum)
        return ret
#法二
"""设动态规划列表 dp，dp[i] 代表以元素 array[i] 为结尾的连续子数组最大和。
状态转移方程： dp[i] = Math.max(dp[i-1]+array[i], array[i]);
具体思路如下：
1.遍历数组，比较 dp[i-1] + array[i] 和 array[i]的大小;
2.为了保证子数组的和最大，每次比较 sum 都取两者的最大值;
3.用max变量记录计算过程中产生的最大的连续和dp[i]；"""