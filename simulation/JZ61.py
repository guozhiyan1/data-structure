"""
法一：
顺子一定没有相等的牌；
2、顺子中两张相邻的扑克牌的数值差为1，即满足interrapt=numbers[i + 1] - numbers[i] - 1==0;
3、当interrapt不为0，代表需要在顺子中插入对应interrapt张牌
interrapt==0,除大小王之外的牌本来就是顺子，大小王随便补齐在头部或者尾部；
(2)interrapt<=zero_num,除大小王之外的牌不是顺子，可以通过大小王变成特定的牌补在其中，使其成为顺子；
(2)interrapt>zero_num,除大小王之外的牌不是顺子,即使有大小王也补不成顺子。
"""
class Solution:
    def IsContinuous(self , numbers: List[int]) -> bool:
        # write code here
        z=numbers.count(0)
        if z>4:
            return False
        numbers.sort()
        b=[]
        for i in range(len(numbers)-1):
            if numbers[i]!=0:
                if numbers[i+1]-numbers[i]==0:
                    return False
                else:
                    b.append(numbers[i+1]-numbers[i])
        for i in range(len(b)):
            if b[i]==1:
                continue
            else:
                if z>=b[i]-1:
                    z=z-b[i]+1
                else:
                    return False
        return True
