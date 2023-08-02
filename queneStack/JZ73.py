class Solution:
    def ReverseSentence(self , str: str) -> str:
        list=[]
        list=str.split()
        if not list:
            return ""
        stack=list.pop()
        while list:
              stack=stack+" "+(list.pop())
        return stack