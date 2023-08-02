# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []  #初始化原栈
        self.stack_min = []  #初始化最小值栈
    def push(self, node):
        self.stack.append(node) #往原栈中添加 元素
        if not self.stack_min:    #一开始也往最小值栈中添加元素
            self.stack_min.append(node)
        elif node < self.stack_min[-1]:  #再次添加元素的时候要同最小值栈中元素比较，小于最小值栈中索引-1的对应值，就把node加入；
            self.stack_min.append(node)
        else:
            self.stack_min.append(self.stack_min[-1])  #否则把索引-1的对应值添加到stack_min中
    def pop(self):
        self.stack.pop()                    #弹出栈顶元素则分别获取即可
        self.stack_min.pop()
    def top(self):
        return self.stack[-1]                #栈顶元素从原栈中获取
    def min(self):
        return self.stack_min[-1]              #最小值就直接从最小值栈中获取
