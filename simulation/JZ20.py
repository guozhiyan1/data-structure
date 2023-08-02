"""表示数值的字符串
法一：正则表达式
字符串["+100","5e2","-123","3.1416","-1E-16,1e-5"]都表示数值。
["12e","1a3.14","1.2.3","+-5","12e+4.3"]都不是数值。
通过对示例的观察可以发现能判断为数值的字符串大致可分为以下四种：
- 是否有前/后 空格或符号位（即 + 、- 两种符号）？
- 是否有整数？
- 是否有小数点？
- 是否有指数e/E？
正则表达式
^为匹配输入字符串的开始位置。
\s匹配空白符的写法
+ 匹配一个或者多个
* 0个或多个
{0,1}   0~1个字符长度
\. 匹配除换行符（\n、\r）之外的任何单个字符
\d 匹配一个数字字符 等价于 [0-9]
(\d)+((\.)(\d)+){0,1}  匹配3.15或100
((\.)(\d)+) .15  ".3e1"    0.3*10
((\d)+(\.))   3.    3.e1    3*10
([eE][+-]{0,1}[\d]+){0,1}
"""
import re
class Solution:
    def isNumeric(self , str: str) -> bool:
        # write code here
        match_Obj = re.match('^\s*[+-]{0,1}((\d)+((\.)(\d)+){0,1}|((\.)(\d)+)|((\d)+(\.)))'
                             '([eE][+-]{0,1}[\d]+){0,1}\s*$',str)
        if match_Obj:
            return True
        else:
            return False
class Solution1:
    def isNumeric(self , str: str) -> bool:
        # write code here
        try:
            float(str)
        except:
            return False
        return True
"""
完全看不懂，不想浪费时间
有限状态自动机
根据字符类型和合法数值的特点，先定义状态
字符类型：
空格 「 」、数字「 0—9 」 、正负号 「 +- 」 、小数点 「 .」 、幂符号 「 eE 」
假设字符串为A.BeC或A.BEC, 也就是整数部分为A，小数部分为B，指数部分为C，按顺序判断是否包含这三部分。
按照字符串从左到右的顺序，定义以下 9 种状态
0. 开始的空格
1. 幂符号前的正负号
2. 小数点前的数字
3. 小数点、小数点后的数字
4. 当小数点前为空格时，小数点、小数点后的数字（意思是没有正数部分，直接以小数点开始）
5. 幂符号（过渡状态）
6. 幂符号后的正负号（过渡状态）
7. 幂符号后的数字
8. 结尾的空格
其中，合法的结束状态有 2, 3, 7, 8
"""
class Solution2:
    def isNumeric(self , str ):
        # write code here
        states = [
            { ' ': 0, 's': 1, 'd': 2, '.': 4 }, # 0. start with 'blank'
            { 'd': 2, '.': 4 } ,                # 1. 'sign' before 'e'
            { 'd': 2, '.': 3, 'e': 5, ' ': 8 }, # 2. 'digit' before 'dot'
            { 'd': 3, 'e': 5, ' ': 8 },         # 3. 'digit' after 'dot'
            { 'd': 3 },                         # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            { 's': 6, 'd': 7 },                 # 5. 'e'
            { 'd': 7 },                         # 6. 'sign' after 'e'
            { 'd': 7, ' ': 8 },                 # 7. 'digit' after 'e'
            { ' ': 8 }                          # 8. end with 'blank'
        ]
        p = 0                           # start with state 0
        for c in str:
            if '0' <= c <= '9': t = 'd' # digit
            elif c in "+-": t = 's' # sign
            elif c in "eE": t = 'e' # e&nbs***bsp;E
            elif c in ". ": t = c # dot, blank
            else: t = '?' # unknown
            if t not in states[p]: return False
            p = states[p][t]
        return p in (2, 3, 7, 8)