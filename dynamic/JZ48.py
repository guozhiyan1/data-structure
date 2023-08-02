"""
主要思路：使用动态规划，记录当前字符之前的最长非重复子字符串长度f(i-1)，其中i为当前字符的位置。每次遍历当前字符时，分两种情况：

1）若当前字符第一次出现，则最长非重复子字符串长度f(i) = f(i-1)+1。
2）若当前字符不是第一次出现，则首先计算当前字符与它上次出现位置之间的距离,假设左边距离最近的相同字符在位置j, 为s[j] , 即s[j]=s[i]。

a. 若res[i-1] < i-j)：即说明前一个非重复子字符串中没有包含当前字符，则可以添加当前字符到前一个非重复子字符串中，所以，f(i) = f(i-1)+1。
b. 若res[i-1[ >= i-j：即说明前一个非重复子字符串中已经包含当前字符，则不可以添加当前字符，所以，dp[i] = i-j。
边界条件和初始条件为

res[0] = 1;

最后返回res中的最大值即可。

其中，字符出现的索引位置通过哈希表进行记录
"abcabcbb"
"""


class Solution:
    def lengthOfLongestSubstring(self , s: str) -> int:
        # write code here
        length=len(s)
        dp={}
        res=tmp=0
        for i in range(length):
            j=dp.get(s[i],-1)
            dp[s[i]]=i
            if tmp < i - j: #前一个非重复子字符串中没有包含当前字符
                tmp=tmp+1
            else:  # 前一个非重复子字符串中已经包含当前字符
                tmp=i-j  #dp[i-1]>dp[i]
            res=max(res,tmp)
        return res

if __name__ == '__main__':
    a="abac"
    b=Solution()
    print(b.lengthOfLongestSubstring(a))