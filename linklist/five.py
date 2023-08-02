class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#哈希图解法
class Solution1:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        node=set()
        while pHead:
            if pHead in node:
                return pHead
            else:
                node.add(pHead)
                pHead=pHead.next
        return None
#双指针法：
# 快慢指针：创建快、慢两个指针（fast、slow），然后fast指针一次走2步；slow指针一次走 1步；如果不存在环，则直接返回None；否则fast、slow指针一定会相遇
#此时再增加一次指针从头开始node每次走1步，它和慢指针第一次相遇就在环节点的入口
class Solution2:
    def EntryNodeOfLoop(self, pHead):
        slow,fast=pHead
        while True:
            if not fast or not fast.next:
                return None
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        node=pHead
        while node!=slow:
            node=node.next
            slow=slow.next
        return node

