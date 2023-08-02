#替换空格
class Solution:
    def replaceSpace(self , s: str) -> str:
        # write code here
        return s.replace(" ", "%20")
#方法：字符串截取相加（推荐使用）
class Solution:
    def replaceSpace(self , s: str) -> str:
        res = ""
        #遍历字符串
        for i in s:
            #非空格直接复制
            if i != ' ':
                res += i
            #空格就替换
            else:
                res += "%20"
        return res
