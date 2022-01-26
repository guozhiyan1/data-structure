#从尾到头打印链表
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def printListFromTailToHead(self,ListNode):
        res=[]
        while(ListNode):
             # res.append(ListNode.val) res[::-1]或res.reverse()
             res.insert(0,ListNode.val)
             ListNode=ListNode.next
        return res
if __name__ == '__main__':
    x={1,2,3}
    a=ListNode(x)
    b=Solution()
    print(b.printListFromTailToHead(a))