class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @return ListNode类
#
class Solution1:
    def deleteDuplication(self , pHead: ListNode) -> ListNode:
        # write code here
        list=self.printcopylink(pHead)
        res=lis=ListNode(0)
        if not pHead:
            return None
        while pHead:
            if pHead.val not in list:
                lis.next=pHead
                lis=lis.next
            pHead=pHead.next
        lis.next=None
        return res.next
    def printcopylink(self,pHead):
        res1=[]
        res=[]
        while pHead:
            res1.append(pHead.val)
            pHead=pHead.next
        for i in range(len(res1)):
            if res1.count(res1[i])!=1:
                res.append(res1[i])
        return res
#循环
class Solution2:
    def deleteDuplication(self , pHead: ListNode) -> ListNode:
        # write code here
        if not pHead:
            return None
        if not pHead.next:
            return pHead
        res=lis=ListNode(0)
        a=-1
        while pHead.next:
            if(pHead.val==pHead.next.val):
                a=pHead.val
            if(pHead.val!=pHead.next.val and a!=pHead.val):
                lis.next=pHead
                lis=lis.next
            pHead=pHead.next
        if(a!=pHead.val):
            lis.next=pHead
            lis=lis.next
        lis.next=None
        return res.next
# 递归
class Solution4:
    def deleteDuplication(self, pHead: ListNode) -> ListNode:
        # write code here
        if not pHead or not pHead.next:
            return pHead
        if pHead.val==pHead.next.val:
            node=pHead.next.next
            while node and pHead.val==node.val:
                node=node.next
            return self.deleteDuplication(node)
        elif pHead.val!=pHead.next.val:
            pHead.next=self.deleteDuplication(pHead.next)
            return pHead