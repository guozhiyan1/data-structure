'''集合唯一性
我们可以对字符串进行两次遍历。在第一次遍历时，我们使用哈希映射统计出字符串中每个字符出现的次数。在第二次遍历时，我们只要遍历到了一个只出现一次的字符，那么就返回该字符，否则在遍历结束后返回空格
'''
class Solution:
    def FirstNotRepeatingChar(self , str: str) -> int:
        # write code here
        a={}
        for i in range(len(str)):
            if str[i] not in a:
                a[str[i]]=i
            else:
                a.pop(str[i])
        if a:
            return min(a.values())
        else:
            return -1
#合适的集合
class Solution:
    def FirstNotRepeatingChar(self , str: str) -> int:
        # write code here
        a={}
        for i in range(len(str)):
            if str[i] not in a:
                a[str[i]]=1
            else:
                a[str[i]]+=1
        if min(a.values())>1:
            return -1
        else:
            b={}
            v=min(a.values())
            name=[key for key,value in a.items() if value==v]
            for i in range(len(str)):
                b[str[i]]=i
            print(name[0])
            print(b)
            return b[name[0]]
#常规解法
class Solution:
    def FirstNotRepeatingChar(self , str: str) -> int:
        # write code here
        if not str:
            return -1
        a=[]
        for i in range(len(str)):
            if i not in a:
                if str[i+1:].find(str[i])==-1:
                    return i
                else:
                    a.append(str[i+1:].find(str[i])+i+1)
        return -1