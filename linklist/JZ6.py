#从尾到头打印链表
"""
1.列表翻转：
a.reverse() 无返回，a本身更改
a[::-1]
在插入的时候  a.insert(0,velue)
List(reversed(a)) 内置函数reversed()函数不对原列表做任何修改，而是返回一个逆序排列后的迭代对象。
2.列表排序
sort(*, key=None, reverse=False)
sorted(iterable, *, key=None, reverse=False)
a.sort()   print(a)
print(list(sorted(a)))
sort 是应用在 list 上的方法，而sorted 可以对所有可迭代的对象进行排序操作；
sort是对原有列表进行操作，而sorted返回的是一个新的可迭代对象，不会改变原来的对象；
sort使用方法为list.sort()， 而sorted的使用方法为sorted(list)


"""
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