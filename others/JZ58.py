#法一 遍历拼接
class Solution:
    def LeftRotateString(self , str, n) -> str:
        # write code here
        if n==0:
            return str
        if not str:
            return ""
        length=len(str)
        if length<n:
            n=n%length
        str=str[n:]+str[0:n]
        return str
#法二 三次反转
"""
输入：  "abcXYZdef",3      返回值："XYZdefabc"
整个字符串反转     fedZYXcba
左边的6个元素反转   XYZdefcba
右边是三个元素反转   XYZdefabc

"""
class Solution:
    def LeftRotateString(self , str: str, n: int) -> str:
        # write code here
        if n==0:
            return str
        if not str:
            return ""
        length=len(str)
        if length<n:
            n=n%length
        a=(list(str))
        a.reverse()
        b=a[0:length-n]
        c=a[length-n:]
        b.reverse()
        c.reverse()
        res=b+c
        st="".join(('%s' %id for id in res))
        return st