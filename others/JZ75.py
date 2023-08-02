#字符流中第一个不重复的字符
class Solution:
    def __init__(self):
        self.l = []
    def FirstAppearingOnce(self):
        for i in self.l:
            if self.l.count(i) == 1: #遍历统计列表字符个数，找到等于1那个就停止遍历
                return i
        return '#'                   #如果不存在=1的，就返回#
    def Insert(self, char):
        self.l += char
#哈希
class Solution1:
    # 返回对应char
    def __init__(self):
        self.a={}

    def FirstAppearingOnce(self):
        for i in self.a:
            if self.a[i]==1:
                return i
        return "#"

        # write code here
    def Insert(self, char):
        # write code
        if char not in self.a:
            self.a[char]=1
        else:
            self.a[char]+=1