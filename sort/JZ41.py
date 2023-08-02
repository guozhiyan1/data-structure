"""数据流中的中位数
传统的寻找中位数的方法便是排序之后，取中间值（奇数）或者中间两位的平均（偶数）即可
但是这道题因为数组在不断增长，每增长一位便需要排一次，很浪费时间，于是可以考虑在增加数据的同时将其有序化，这个过程就让我们想到了插入排序：
对于每个输入的元素，遍历已经有序的数组，将其插入到属于它的位置。
"""
class Solution:
    def __init__(self):
        self.val = []
    def Insert(self, num):
        if len(self.val) == 0:
            #val中没有数据，直接加入
            self.val.append(num)
        #val中有数据，需要插入排序
        else:
            i = 0
            #遍历找到插入点
            while i < len(self.val):
                if num <= self.val[i]:
                   break
                i = i + 1
            #插入相应位置
            self.val.insert(i, num)
    def GetMedian(self):
        n = len(self.val)
        #奇数个数字
        if n % 2 == 1:
            #类型转换
            return self.val[n // 2]
        #偶数个数字
        else:
            return (self.val[n // 2] + self.val[n // 2 - 1]) / 2.0
"""
法二我们来看看中位数的特征，它是数组中间个数字或者两个数字的均值，它是数组较小的一半元素中最大的一个，同时也是数组较大的一半元素中最小的一个。
那我们只要每次维护最小的一半元素和最大的一半元素，并能快速得到它们的最大值和最小值，那不就可以了嘛。这时候就可以想到了堆排序的优先队列
step 1：我们可以维护两个堆，分别是大顶堆min，用于存储较小的值，其中顶部最大；小顶堆max，用于存储较大的值，其中顶部最小，则中位数只会在两个堆的堆顶出现。
step 2：我们可以约定奇数个元素时取大顶堆的顶部值，偶数个元素时取两堆顶的平均值，则可以发现两个堆的数据长度要么是相等的，要么奇数时大顶堆会多一个。
step 3：每次输入的数据流先进入大顶堆排序，然后将大顶堆的最大值弹入小顶堆中，完成整个的排序。
step 4：但是因为大顶堆的数据不可能会比小顶堆少一个，因此需要再比较二者的长度，若是小顶堆长度小于大顶堆，需要从大顶堆中弹出最小值到大顶堆中进行平衡。

"""
import heapq
class Solution:
    def __init__(self):
        #小顶堆，元素数值都比大顶堆大 要创建一个堆，可以使用list来初始化为 [] ，或者你可以通过一个函数 heapify() ，来把一个list转换成堆
        self.max = []
        #大顶堆，元素数值较小，加入元素要乘-1才能实现大顶堆，取出时也要乘-1还原
        self.min = []
    def Insert(self, num):
        #先加入较小部分
        heapq.heappush(self.min, (-1 * num))
        #将较小部分的最大值取出，送入到较大部分
        heapq.heappush(self.max, -1 * self.min[0])
        heapq.heappop(self.min)
        #平衡两个堆的数量
        if len(self.min) < len(self.max):
            heapq.heappush(self.min, -1 * self.max[0])
            heapq.heappop(self.max)
    def GetMedian(self):
        #奇数个
        if len(self.min) > len(self.max):
            return self.min[0] * -1.0
        else:
            #偶数个
            return (-1 * self.min[0]  + self.max[0]) / 2
