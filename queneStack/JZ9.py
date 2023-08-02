#两个栈实现队列 123 栈：3，2，1 队列：1，2，3 所以要反一下
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx 如何不判stack2空的话["PSH2","PSH3","POP","PSH1","POP","POP"] 执行结果为2,1,3 期望结果为2,3,1
        '''不判空：                         判空
        stack1：2，3，1                      stack1：2，3，1
        stack2：3，1                         stack2：3，1
        结果：2  1  3                        结果：2  3  1
        '''
        if not self.stack2:
            for i in range(len(self.stack2)):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()