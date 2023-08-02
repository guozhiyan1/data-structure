#第一种方法遍历
class Solution:
    def StrToInt(self, s: str) -> int:
        # write code here
        s = s.strip()
        if not s:
            return 0
        flag = True
        index=0
        res = 0
        weight=0
        if ord(s[0]) < 48 or ord(s[0]) > 57:
            if ord(s[0])!= 45 and ord(s[0]) != 43:
                return 0
        for i in range(len(s)):
            if ord(s[i])==48:
                weight+=1
            if ord(s[i])>=48 and ord(s[i])<=57:
                res=res*10+int(s[i])
            elif s[i]=="+" or s[i]=="-":
                if index==0 and res==0 and weight==0:
                    index+=1
                    if s[i]=="+":
                        flag=True
                    else:
                        flag = False
                else:
                    if res!=0 and weight==0:
                        break
                    else:
                        return 0
            else:
                break
        if flag:
            return min(2 ** 31 - 1,res)
        else:
            return max(-res,-2 ** 31)

#参考
class Solution:
    def StrToInt(self , s: str) -> int:
        res = 0
        index = 0
        #去掉前导空格
        s = s.strip()
        #去掉空格就什么都没有了
        n = len(s)
        if s == "":
            return 0
        sign = 1
        #处理第一个符号是正负号的情况
        if s[index] == '+':
            index += 1
        elif s[index] == '-':
            index += 1
            sign = -1
        #去掉符号就什么都没有了
        if index == n:
            return 0
        while index < n:
            c = s[index]
            #后续非法字符，截断
            if c < '0' or c > '9':
                break
            #转数字
            res = res * 10 + sign * ((int)(c) - (int)('0'))
            index += 1
        #输出处理越界
        return min(max(res, -2 ** 31), 2 ** 31 - 1)
#第二种方法 状态机
"""
字符串无非就是这些类型：[ ' '（空格）, 0（前导或者数字中间的）, [1-9], 其它非法字符，'-/+' ]我们可以将其映射成数字： [0,1,2,3,4]
空格去掉后一共有4种状态 0，1，2，3  kanbudong
"""
class Solution:
    def StrToInt(self , s: str) -> int:
        #状态转移矩阵
        states = [[0,1,2,3,1],
                 [3,1,2,3,3],
                 [3,2,2,3,3]]
        res = 0
        #与int边界比较
        top = 2 ** 31 - 1
        bottom = -2 ** 31
        n = len(s)
        sign = 1
        #状态从“ ”开始
        state = 0
        for i in range(n):
            c = s[i]
            if c == ' ':
                #空格
                state = states[state][0]
            elif c == '0':
                #前导0或者中间的0
                state = states[state][1]
            elif c >= '1' and c <= '9':
                #数字
                state = states[state][2]
            elif c == '-' or c == '+':
                #正负号
                state = states[state][4]
                if state == 1:
                    sign = -1 if(c == '-') else 1
                else:
                    break
            else:
                #非法字符
                state = states[state][3]
            if state == 2:
                #数字相加
                res = res * 10 + ((int)(c) - (int)('0'))
                #越界处理
                res = min(res, top) if(sign == 1) else min(res, -bottom)
            if state == 3:
                break
        return sign * res
