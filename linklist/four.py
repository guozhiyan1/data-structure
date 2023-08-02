"""大概看下思路"""
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
#暴力循坏 可以运行
class solution1:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        p1, p2 = pHead1, pHead2
        while p1:
            while p2:
                while (p1 == p2): #这一步特别重要，不仅是值相等，指针也要相等
                    return p1
                p2 = p2.next
            p2 = pHead2
            p1 = p1.next
        return None
#统计两个链表的长度，先找出两个链表的长度，最后去掉长链表多的部分，剩下一样长度的从头开始遍历，到相同的就是公共结点了
class solution2:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        len1=self.size(pHead1)
        len2=self.size(pHead2)
        l=len1-len2
        while(l>0):
            pHead1=pHead1.next
            l=l-1
        while(l<0):
            pHead2 = pHead2.next
            l = l + 1
        while pHead1:
            if(pHead1==pHead2):
                return pHead1
            pHead1=pHead1.next
            pHead2=pHead2.next
        return None
    def size(self,phead):
        l=0
        while phead:
            l=l+1
            phead=phead.next
        return l
#双指针法：使用两个指针 a，b 分别指向两个链表 pHead1，pHead2的头结点，然后同时分别逐结点遍历，当 a 到达链表 pHead1的末尾时，重新定位到链表 pHead2的头结点；当 b 到达链表 pHead2 的末尾时，重新定位到链表 pHead1的头结点。当双指针相遇时，所指向的结点就是第一个公共结点
#这道题的精髓在于if a，如果两个链表没有公共结点，第一次两个链表加在一起后第二次返回的none也会相等而结束循坏，
class solution3:
    def FindFirstCommonNode(self, pHead1, pHead2):
        a=pHead1
        b=pHead2
        while a!=b:
            a=a.next if a else pHead2
            b=b.next if b else pHead1
        return a
#第一种就是把全部结点分别压入两个栈，利用栈的特性LIFO，然后同时pop出栈，相同的时候就是第一个公共结点
class solution4:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        stack1=[]
        stack2=[]
        while pHead1:
            stack1.append(pHead1)
            pHead1=pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2=pHead2.next
        node = None
        while stack1 and stack2:
            p1=stack1.pop()
            p2=stack2.pop()
            if(p1==p2):
                node =p1
        return node
#集合去重
class Solution5:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        node=set()
        while pHead1:
            node.add(pHead1)
            pHead1=pHead1.next
        while pHead2:
            if pHead2 in node:
                return pHead2
            else:
                pHead2=pHead2.next
        return None





