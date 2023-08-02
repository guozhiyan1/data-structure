#返回倒数第k个结点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#时间复杂度O(n)  空间复杂度O(1)
class Solution1:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        # write code here
        l=self.size(pHead)
        if(k>l):
            return None
        t=l-k
        while (t>0):
            pHead=pHead.next
            t=t-1
        return pHead
    def size(self,pHead):
        l=0
        while pHead:
            l=l+1
            pHead=pHead.next
        return l
#快慢指针；第一个指针先移动k步骤，然后两个指针同时移动，当第一个指针走到终点的时候，返回第二个指针
class Solution2:
    def FindKthToTail(self, pHead: ListNode, k: int) -> ListNode:
        fast = slow = pHead
        while k > 0:
            if fast:
                fast = fast.next
                k = k - 1
            else:
                return None
        while fast:
            fast = fast.next
            slow = slow.next
        return slow

#栈 把原链表的结点全部压栈，然后再把栈中最上面的k个节点出栈，出栈的结点重新串成一个新的链表即可
class Solution3:
    def FindKthToTail(self, pHead: ListNode, k: int) -> ListNode:
        stack=[]
        while pHead:
            stack.append(pHead)
            pHead=pHead.next
        if k>len(stack) or not k:
            return None
        return stack[-k]