#复杂链表的复制
# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
import copy
class Solution1:
    # 返回 RandomListNode
    def Clone(self, pHead):
        ret=copy.deepcopy(pHead)
        return ret
#递归
class Solution2:
    # 返回 RandomListNode
    def Clone(self, pHead):
        node = RandomListNode(None)
        head = node
        while pHead:
            node.next = RandomListNode(pHead.label)
            node = node.next
            node.next = pHead.next
            node.random = pHead.random
            pHead = pHead.next
        return head.next
#循环 方法1：在A后面加A，最后再拆下来
class Solution2:
    class Solution3:
        def Clone(self, pHead):
            if not pHead:
                return None
            # 把复制的结点链接在原始链表的每一对应结点后面
            head=pHead
            while head:
                node=RandomListNode(head.label)
                node.next = head.next
                head.next=node
                head=node.next
            # 把复制的结点的random指针指向被复制结点的random指针的下一个结点
            head=pHead
            while head:
                if head.random:
                    head.next.random=head.random.next
                head=head.next.next
            # 拆分成两个链表(注意复制链表的最后一个结点的next指针不能跟原链表指向同一个空结点None，next指针要重新赋值None(判定程序会认定你没有完成复制）)
            head=pHead
            pHead=pHead.next
            while head.next:
                node=head.next
                head.next=node.next
                head=node
            return pHead