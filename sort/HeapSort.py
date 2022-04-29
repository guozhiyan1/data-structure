"""
堆排序的基本思想：
（1）将带排序的序列构造成一个大顶堆，根据大顶堆的性质，当前堆的根节点（堆顶）就是序列中最大的元素；
（2）将堆顶元素和最后一个元素交换，然后将剩下的节点重新构造成一个大顶堆；
（3）重复步骤2，如此反复；
（4）从第一次构建大顶堆开始，每一次构建，我们都能获得一个序列的最大值，然后把它放到大顶堆的尾部。
（5）最后，就得到一个有序的序列了

"""
class Solution:
    def heapsort(self,nums):
        length=len(nums)
        for i in range(length,-1,-1):#5,4,3,2,1,0
            self.heapify(nums,length,i)
        for i in range(length-1,0,-1):#4,3,2,1 len=5
            nums[i],nums[0]=nums[0],nums[i]
            self.heapify(nums,i,0)
        return nums

    def heapify(self,nums,length,i):
        largest=i
        left=2*i+1
        right=2*i+2
        if left<length and nums[i]<nums[left]:
            largest=left
        if right<length and nums[largest]<nums[right]:
            largest=right
        if largest!=i:
            nums[i],nums[largest]=nums[largest],nums[i]
            self.heapify(nums,length,largest)
if __name__ == '__main__':
    a=Solution()
    nums=[4,5,8,2,3,9,7,1]
    print(a.heapsort(nums))