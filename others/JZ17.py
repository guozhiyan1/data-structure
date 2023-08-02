class Solution:
    def printNumbers(self , n: int) -> List[int]:
        # write code here
        l=0
        for i in range(1,n+1):
            k=(pow(10,i-1))
            l=k*9+l
        return list(range(1,l+1))
class Solution:
    def printNumbers(self , n: int) -> List[int]:
        #找到该n+1位数的最小数字
        end = 10 ** n
        #从1遍历到n+1位数的最小数字输出
        return list(range(1,end))
