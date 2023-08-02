"""
堆排序的基本思想：
（1）将带排序的序列构造成一个大顶堆，根据大顶堆的性质，当前堆的根节点（堆顶）就是序列中最大的元素；
（2）将堆顶元素和最后一个元素交换，然后将剩下的节点重新构造成一个大顶堆；
（3）重复步骤2，如此反复；
（4）从第一次构建大顶堆开始，每一次构建，我们都能获得一个序列的最大值，然后把它放到大顶堆的尾部。
（5）最后，就得到一个有序的序列了

"""
class Solution:
    def adjust_heap(self,nums, i, length):
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        max = i
        if i < length / 2:
            if lchild < length and nums[lchild] > nums[max]:
                max = lchild
            if rchild < length and nums[rchild] > nums[max]:
                max = rchild
            if max != i:
                nums[max], nums[i] = nums[i], nums[max]
                self.adjust_heap(nums, max, length)

    def build_heap(self,nums): #构建大根堆
        length=len(nums)
        for i in range(0, (length // 2))[::-1]:
            self.adjust_heap(nums, i, length)

    def heapsort(self,nums):
        length = len(nums)
        self.build_heap(nums)
        for i in range(length-1,-1,-1): #6~0
            nums[0], nums[i] = nums[i], nums[0]  #将堆顶元素和最后一个元素交换
            self.adjust_heap(nums, 0, i)#剩下的i-1个元素构建大根堆
if __name__ == '__main__':
    a=Solution()
    nums=[70,60,12,40,30,8,10]
    a.heapsort(nums)
    print(nums)