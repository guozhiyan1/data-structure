class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        # write code here
        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i][j]==target:
                    return True
        return False
#主要在于选择合适的位置才能使用二分法法
class Solution1:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        # write code here
        m=len(array)
        if m==0:
            return False
        n=len(array[0])
        if n==0:
            return False
        i=0
        j=n-1
        while(i<m and j>=0):
            if target==array[i][j]:
                return True
            elif target>array[i][j]:
                i=i+1
            else:
                j=j-1
        return False