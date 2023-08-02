"""
暴力或归纳解法
跳台阶
1,1   1
2,2   1   2
3,3   12   21
4,5     1111    112,121,211，22
5,8  11111,2111,1211,1121,1112,221,122,212，
我们在列举的时候，可以使用一个小技巧。比如列举 f(4) 的所有可能时，先列举不跳2级台阶的可能，再列举跳了1次2级台阶的可能，再列举跳了2次2级台阶的可能
f(n)=f(n-1)+f(n-2)
"""
class Solution1:
    def jumpFloor(self , number: int) -> int:
        # write code here
        if number==1 or number==2:
            return number
        return self.jumpFloor(number-1)+self.jumpFloor(number-2)
class Solution2:
    def jumpFloor(self , number: int) -> int:
        # write code here
        if number==1 or number==2:
            return number
        a=1
        b=2
        while(number>=3):
            a,b=b,a+b
            number=number-1
        return b