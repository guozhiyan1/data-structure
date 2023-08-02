"""
礼物的最大价值
确定状态 （重复子问题且子问题可以自己解决不依赖其他步骤）：结束，最后一步，右下角走到了grid[m][n]结束，所以它上一步就是gird[m-1][n]或 grid[m][n-1]
状态转移方程 f(x,y)=max{f(x,y-1),f(x-1,y}+grid[m][n]
初始条件 f(0,0)=grid[0,0]
边界情况，如果矩阵为3*3，[0,2]下一步只能[1,2]

"""


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # write code here
        """动态规划：[[0]*m]*n   dp[0][0]=List[0][0]
        next=dp[0][0]+dp[0][1]      dp[0][0]+dp[1][0]
        next=dp[0][2] or dp[1][1]    比当前大，不一定总数大。
        """
        m = len(grid)
        n = len(grid[0])

        maxprice = grid[0][0]
        i, j = 0, 0
        while (0 <= i < m and 0 <= j < n):
            if i == m - 1 and j == n - 1:
                break
            if i == m - 1 or (grid[i][j + 1] > grid[i + 1][j]):
                maxprice += grid[i][j + 1]
                j = j + 1
            elif j == n - 1 or (grid[i][j + 1] <= grid[i + 1][j]):
                maxprice += grid[i + 1][j]
                i = i + 1
        return maxprice
class Solution:
    def maxValue(self , grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[0][0]=grid[0][0]
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[-1][-1]