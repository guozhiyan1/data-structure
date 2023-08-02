'''二叉树的下一个结点
题目：给二叉树和其中一个结点，返回中序遍历顺序的下一个结点
{8,6,10,5,7,9,11},8     中序遍历结果为5,6,7,8,9,10,11，8后面是9
如图：中序遍历结果为4,2,5,1,3,7,6
点的下一个结点，有三种可能的情况：

根据中序遍历规则，我们先看被指向的节点有无右子树
！如果有，再看右子树有没有左节点
！！如果右子树没有左节点，就返回右子树
！！如果右子树有左节点，就一直往下找左节点，直到叶子节点为止，返回叶子节点

！如果被指向节点没有右子树，就看他的父节点：
！！如果被指向节点是其父节点的左子树，就返回其父节点
！！如果被指向节点是其父节点的右子树，就继续寻找父节点的父节点
'''
# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if pNode.right:
            tmpNode=pNode.right
            while tmpNode.left:
                tmpNode=tmpNode.left
            return tmpNode
        while pNode.next:
            parent=pNode.next
            if parent.left==pNode:
                return parent
            pNode=parent
        return None
