class Solution:
    def __init__(self):
        self.res = 0
    def Sum_Solution(self , n: int) -> int:
        # write code here
        n>1 and self.Sum_Solution(n-1)
        self.res+=n
        return self.res