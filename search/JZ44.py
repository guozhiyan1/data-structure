"""
//比较详细了
    /*
    1-9       9个*1
    10-99     90个*2
    100-999   900个*3
    1000-9999 9000个*4
    */
"""
class Solution:
    def findNthDigit(self , n: int) -> int:
        # write code here
        if n<=9:
            return n
        if 10<=n<=29:
            if n%2==0:
                return 1
            else:
                return （n-11）/2
        elif 30<=n<59:
            if n%2==0:
                return 2
            else:
                return (n-31)/2