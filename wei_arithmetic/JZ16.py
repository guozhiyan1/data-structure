class Solution:
    def Power(self , base: float, exponent: int) -> float:
        # write code here
        res=1
        if exponent>0:
            while exponent:
                res=res*base
                exponent-=1
            return res
        elif exponent<0:
            a=self.Power(base, -exponent)
            return 1/a
        else:
            return res