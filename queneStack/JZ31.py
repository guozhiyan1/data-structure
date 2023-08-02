#栈的压入、弹出序列；输入[1,2,3,4,5],[4,5,3,2,1]返回true;输入[1,2,3,4,5],[4,3,5,1,2]，返回false
#辅助栈
"""准备一个辅助栈，两个下标分别访问两个序列辅助栈为空或者栈顶不等于出栈数组当前元素，就持续将入栈数组加入栈中栈顶等于出栈数组当前元素就出栈。当入栈数组访问完，出栈数组无法依次弹出，就是不匹配的，否则两个序列都访问完就是匹配的"""
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
# -*- coding:utf-8 -*-
class Solution4:
    def IsPopOrder(self, pushV, popV):
        # write code here
        #不用辅助栈，直接把pushV当作stack来处理
        i = j = 0
        for x in pushV:
            pushV[i] = x                                     #直接把pushV当作压入栈
            while i >= 0 and pushV[i] == popV[j]:            #当pushV的当前元素等于popV弹出列的顶部元素
                i, j = i - 1, j + 1                          #分别更新栈顶元素
            i += 1                                           #否则继续往pushV压入栈中添加元素
        return i == 0                                         #直到pushV的索引减小为0
class Solution2:
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
class Solution3:
    def IsPopOrder(self , pushV: List[int], popV: List[int]) -> bool:
        # write code here
        stack=[]
        while pushV:
            if pushV[0]==popV[0]:
                pushV.pop(0)
                popV.pop(0)
            elif stack and stack[-1]==popV[0]:
                stack.pop()
                popV.pop(0)
            else:
                stack.append(pushV.pop(0))
        for i in range(len(stack)):
            if stack[0]==popV[-1]:
                stack.pop(0)
                popV.pop()
        if not popV or popV==pushV:
            return True
        else:
            return False