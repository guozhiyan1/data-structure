"""
数字以 0123456789101112131415... 的格式作为一个字符序列，在这个序列中第 2 位（从下标 0 开始计算）是 2 ，第 10 位是 1 ，第 13 位是 1 ，以此类题，请你输出第 n 位对应的数字
//比较详细了
    /*
    0-9       10个*1
    10-99     90个*2
    100-999   900个*3
    1000-9999 9000个*4
    */
    求1001位，首先1001-9-90*2=812<2700 所以是三位数,且是三位数中第812个数   812=270*3+2;所以第812位是从100开始的第270个数值的第二个数字，就是7
    number=100+812/3=370  idx=n % digits=2    812%3=2
    370第二位就是7
"""
class Solution:
    def findNthDigit(self , n: int) -> int:
        # write code here
        if n==0:
            return 0
        digits=1
        length=self.countDigit(digits)
        while n>=length:
            if n-length<=0:
                break
            n=n-length
            digits+=1
            length=self.countDigit(digits)*digits      #算出digits=3.剩余n=812
        idx=n%digits
        number=pow(10,digits-1)+n//digits    #三位数从100开始，四位数从1000
        if digits==1:
            return n
        else:
            return int(str(number)[idx-1]) # 答案就是number的idx-1位数

    def countDigit(self,digits):
        #根据输入的数字，判断digit位的数字有多少个;确定这个n位在几位数字中
        if digits==1:
            return 9
        return 9* pow(10,digits-1)
