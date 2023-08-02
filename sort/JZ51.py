#暴力法
def InversePairs(self, data: List[int]) -> int:
    # write code here
    count = 0
    for i in range(1, len(data)):
        for j in range(0, i):
            if data[i] < data[j]:
                count += 1
    return count % 1000000007
#法二 归并排序思想
class Solution:
    def __init__(self):
        self.count=0
    def InversePairs(self , data: List[int]) -> int:
        self.MergeSort(data)
        return self.count%1000000007
    def MergeSort(self , data: List[int]) -> int:
        # write code here
        if len(data)<2:
            return data
        mid=len(data)//2
        s1=self.MergeSort(data[0:mid])
        s2=self.MergeSort(data[mid:])
        return self.Merge(s1,s2)
    def Merge(self,s1,s2):
        i=j=0
        a=[]
        while i<len(s1) and j<len(s2):
            if s1[i]<s2[j]:
                a.append(s1[i])
                i+=1
            elif len(s1)!=1:
                self.count=self.count+(len(s1[i:]))
                a.append(s2[j])
                j+=1
            else:
                self.count+=1
                a.append(s2[j])
                j+=1
        a=a+s1[i:]+s2[j:]
        return a