#字符串的排列
'''
两个字符： 0,1         1，0
三个字符：0     1，2
      1       0，2
      2       0，1
      ABC [0:0]  A      BC
          [0:1]   B     A+bc
          [0:2]   C     AB+c
'''
class Solution:
    def Permutation(self , str):
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
if __name__ == '__main__':
    s=Solution()
    print(s.Permutation("ABC"))