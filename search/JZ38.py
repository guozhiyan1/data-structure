#字符串的排列
'''
两个字符： 0,1         1，0
三个字符：0     1，2
      1       0，2
      2       0，1
'''
class Solution:
    def Permutation(self , str: str) -> List[str]:
        # write code here
        length=len(str)
        if length<=1:
            return str
        b=[]
        for i in range(length):
            first=str[i]
            last=str[:i]+str[i+1:]
            for j in self.Permutation(last):
                str1=first+j
                if str1 not in b:
                    b.append(str1)
        return b