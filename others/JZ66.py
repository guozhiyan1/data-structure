"""
#双向遍历
step 1：初始化数组B，第一个元素为1.
step 2：从左到右遍历数组A，将数组B的前一个数与数组A的前一个数相乘就得到了下三角中数组B的当前数。
step 3：再从右到左遍历数组A，用一个数字记录从右到左上三角中的累乘，每次只会乘上一个数，同时给数组B对应部分也乘上该累乘。


"""
class Solution:
    def multiply(self , A):
        #初始化数组B
        B = [1 for _ in range(len(A))]
        #先乘左边，从左到右
        for i in range(1, len(A)):
            #每多一位由数组B左边的元素多乘一个前面A的元素
            B[i] = B[i - 1] * A[i - 1]     #B[i]=A[0]*A[1]*...A[n-1]
        temp = 1
        for i in range(len(A)-2,-1,-1):
            #temp为右边的累乘
            temp *= A[i+1]
            B[i] *= temp
        return B
if __name__ == '__main__':
    a=Solution()
    s=[1,2,3,4]
    b=a.multiply(s)
    print(b)