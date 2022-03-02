#栈的压入、弹出序列；输入[1,2,3,4,5],[4,5,3,2,1]返回true;输入[1,2,3,4,5],[4,3,5,1,2]，返回false
#辅助栈
class Solution1:
    def IsPopOrder(self , pushV, popV) -> bool:
        stack=[]
        j=0
        for x in pushV:
            stack.append(x)
            while stack and stack[-1]==popV(j):
                stack.pop()
                j=j+1
        return j==len(popV)
#代码优化  不用辅助栈
class Solution:
    def IsPopOrder(self , pushV: List[int], popV: List[int]) -> bool:
        # write code here
        stack=[]
        j=0
        while j<len(pushV):
                if pushV[j]!=popV[0] and not stack:
                    stack.append(pushV[j])
                    j=j+1
                elif stack and pushV[j]!=popV[0] and stack[-1]!=popV[0]:
                    stack.append(pushV[j])
                    j=j+1
                elif stack and stack[-1]==popV[0]:
                    popV.pop(0)
                    stack.pop()
                else:
                    popV.pop(0)
                    j=j+1
        while stack:
            if stack[-1]==popV[0]:
                popV.pop(0)
                stack.pop()
            else:
                break
        if not popV:
            return True
        else:
            return False