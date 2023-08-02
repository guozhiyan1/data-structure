#排序两个递增链表
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
#迭代
class solution1:
    def Merge(self , pHead1: ListNode, pHead2: ListNode):
        if not pHead2:
            return pHead1
        if not pHead1:
            return pHead2
        result=cur=ListNode(0)
        while pHead1 and pHead2:
            if(pHead1.val<pHead2.val):
                cur.next=pHead1
                pHead1=pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur=cur.next
        while pHead1:     #cur.next = pHead1 if pHead1 else pHead2
            cur.next=pHead1
            pHead1 = pHead1.next
            cur = cur.next
        while pHead2:
            cur.next=pHead2
            pHead2 = pHead2.next
            cur = cur.next
        return result.next
#递归
class solution1:
    def Merge(self, pHead1: ListNode, pHead2: ListNode):
        if not pHead2:
            return pHead1
        if not pHead1:
            return pHead2
        result = cur = ListNode(0)
        if (pHead1.val < pHead2.val):
            cur.next = pHead1
            cur.next.next = self.Merge(pHead1.next, pHead2)
        else:
            cur.next = pHead2
            cur.next.next = self.Merge(pHead1, pHead2.next)
        return result.next


