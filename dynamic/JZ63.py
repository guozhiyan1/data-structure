"暴力算法"
class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        # write code here i是买入天，j是卖出天，j>i，返回最大值
        length=len(prices)
        if length<=1:
            return 0
        result=[]
        for i in range(length):
            for j in range(i+1,length):
                result.append(prices[j]-prices[i])
        return max(result)if max(result)>0 else 0
"""动态规划

两天的时候      prices[j-i]  小于0取0   2,  4
三天的时候  前两天比较买最低的   卖出后两天比较取最高的   2,4    ，4,1
四天的时候   前三天比较买最低的       后三天比较取最高的     且买卖一定要隔一天 
buy=for   prices[0:length-1]
sell=for   prices[1:length]  
查找规律：最低买，最高卖  查找最低值2，在3,4,5，6最高值7，得出5
[8,9,2,5,4,7,1]
状态定义：
dp[i][j]：下标为 i 这一天结束的时候，手上持股状态为 j 时，我们持有的现金数。
    j = 0，表示当前不持股；
    j = 1，表示当前持股。
注意：这个状态具有前缀性质，下标为 i 的这一天的计算结果包含了区间 [0, i] 所有的信息，因此最后输出 dp[len - 1][0]

推导状态转移方程：
dp[i][0]：规定了今天不持股，有以下两种情况：
    昨天不持股，今天什么都不做；
    昨天持股，今天卖出股票（现金数增加），
    状态转移方程：dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
dp[i][1]：规定了今天持股，有以下两种情况：
    昨天持股，今天什么都不做（现金数与昨天一样）；
    昨天不持股，今天买入股票（注意：只允许交易一次，因此手上的现金数就是当天的股价的相反数）
    状态转移方程：dp[i][1] = Math.max(dp[i - 1][1], -prices[i]);
    [8,9,2,5,4,7,1]
"""
class Solution:
    def maxProfit(self , prices ):
        # write code here
        length = len(prices)
        if length <2:
            return 0
        dp = [[0]*2]*(length)
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,length):
            dp[i][0] =  max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],-prices[i])
        return dp[length-1][0]
"""
这套算法的核心思路在于固定买入的价格，寻找在此买入价下可能的最大收益，然后在所有的最大收益中找到最大收益，当然也可以反过来固定最大价格，往前找最小值计算，结果是一样的。

算法缺点在于嵌套循环非常的费时间，还有优化空间，看看大神们的答案"""
class Solution:
    def maxProfit(self , prices ):
        # write code here
        maxPro = 0                                   #初始化最大收益为0
        for i in range(len(prices)):
            curPro = 0                               #初始化当前收益为0
            maxPrice = prices[i]                     #找后面比第一个大的价格，所以这里要初始化最大价格为当前价格
            for j in range(i,len(prices)):
                maxPrice = max(maxPrice,prices[j])   #轮次比较，找后面最大的价格
            curPro = maxPrice - prices [i]           #最大的价格减第一个价格就是当前的最大收益了
            if curPro > maxPro:
                maxPro = curPro                      #更新最大收益
        return maxPro