"""
用辅助数组dp表示前i个数的译码方法有多少种
输入: 12258
输出: 5 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
单独翻译，即是 [1, 2 ,2, 5, 8]
[1, 22, 5, 8] 对应翻译的是 "bwfi"
[1, 2, 25, 8] 对应翻译的是 "bczi"
[12, 2, 5, 8] 对应翻译的是 "mcfi"
[12, 25, 8] 对应翻译的是 "mzi"
对于一个数，我们可以直接译码它，也可以将其与前面的1或者2组合起来译码;
如果直接译码，则dp[i]=dp[i−1]；
如果组合译码，i-2有 dp[i−2]种翻译方案+  则dp[i]=dp[i−2]。
"""
class Solution:
    def solve(self , nums: str) -> int:
        #排除0
        if nums == "0":
            return 0
        #排除只有一种可能的10 和 20
        if nums == "10" or nums == "20":
            return 1
        #当0的前面不是1或2时，无法译码，0种
        for i in range(1, len(nums)):
            if nums[i] == '0':
                if nums[i - 1] != '1' and nums[i - 1] != '2':
                    return 0
        #辅助数组初始化为1
        dp = [1 for i in range(len(nums) + 1)]
        for i in range(2, len(nums) + 1):
            #在11-19，21-26之间的情况
            if (nums[i - 2] == '1' and nums[i - 1] != '0') or (nums[i - 2] == '2' and nums[i - 1] > '0' and nums[i - 1] < '7'):
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[len(nums)]