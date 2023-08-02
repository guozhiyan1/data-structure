class Solution:
    def match(self , str , pattern ):
        if not pattern:                   #1.特殊情况，不存在匹配模式，那么就没有匹配字符串
            return not str
         #2. 递归的终止条件f(1) = 1：在这里就是 首位即匹配。
        first_match = str and pattern[0] in {str[0], '.'}
        #如果模式长度 >= 2,并且 模式索引[1] == '*'情况，也要分两种：1.模式中的字符'.'表示任意一个字符2.模式中的字符'*'表示它前面的字符可以出现任意次（包含0次）
        if len(pattern) >= 2 and pattern[1] == '*':
            #第一种就是模式长度>2的情况下：字符串完全匹配从模式索引2之后的位置   aad","c*a*d"
            return (self.match(str, pattern[2:]) or
                    #或者模式长度 =2的情况下：字符串从索引1位置开始，完全匹配模式  aab    a*b
                    first_match and self.match(str[1:], pattern))
        else:
        #否则，模式长度>=2,而模式索引从1开始是 点字符或 *字符在其他位置，
            return first_match and self.match(str[1:], pattern[1:])
"""
动态规划：
最优子结构：str长度i，pattern长度是j，从str[:1]和pattern[:1]是否匹配开始判断，直至添加完整字符串。
添加下一个字符时分别添加， “aaa” "ab*ac" a和a匹配后确认aa和a以及a和ab能否匹配
状态转移方程：状态定义：dp[i][j]

"""

