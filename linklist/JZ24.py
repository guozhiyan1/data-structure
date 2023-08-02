#反转链表、
"""经常不会，重点看"""
import sys
sys.setrecursionlimit(1000000)
class ListNode:
    def __init__(self,x):
        self.next=None
        self.val=x
#迭代
class Solution1:
    def ReverseList(self , head: ListNode):
        if not head:
            return None
        cur=head.next
        pre=head
        pre.next=None
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre
#递归
class Solution2:
    def ReverseList(self, head: ListNode):
        if not head:
            return None
        if  head.next == None:
            return head
        new_head = self.ReverseList(head.next)         #层层递归找到最后一个结点
        head.next.next=head                #只处理两个结点的情况
        head.next=None
        return new_head



