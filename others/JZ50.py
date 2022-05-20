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