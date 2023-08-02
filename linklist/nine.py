class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param val int整型
# @return ListNode类
#
class Solution1:
    def deleteNode(self , head: ListNode, val: int) -> ListNode:
        # write code here.
        res=self.printlink(head)
        result=lis=ListNode(-1)
        for i in range(len(res)):
            if res[i]!=val:
                lis.next=head
                lis=lis.next
            head=head.next
        return  result.next
    def printlink(self,pHead):
        res=[]
        while pHead:
            res.append(pHead.val)
            pHead=pHead.next
        return res
class Solution2:
    def deleteNode(self , head: ListNode, val: int) -> ListNode:
        # write code here.
        result=lis=ListNode(-1)
        while head:
            if head.val!=val:
                lis.next=head
                lis=lis.next
            head=head.next
        return  result.next
import sys
sys.setrecursionlimit(1000000)
class Solution3:
    def deleteNode(self , head: ListNode, val: int) -> ListNode:
        # write code here.
        if not head:
            return None
        res=lis=ListNode(-1)
        if head.val!=val:
            lis.next=head
            lis=lis.next
        lis.next=self.deleteNode(head.next, val)
        return  res.next