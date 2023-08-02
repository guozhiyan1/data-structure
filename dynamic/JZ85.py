#注意特殊的情况[-1,-2,-3,-4]
"""
# 用动态规划求一个连续数组最大和的时候，是一个dp数组，这个数组里面最大值才是最大和，
# 那么问题是如何根据这个dp最长子数组呢？
# 方法如下：
# 在求得dp的同时记录当前的dp的数组范围
# 如果当前dp是单个元素则要重置索引，
# 如果当前dp是最大值则要把当前索引保存起来为最大长度和最大索引范围，
# 特殊情况是如果当前dp是已经存在的最大值，
# 则需要考虑当前索引范围是否大于最大索引范围，如果是则更新
"""
class Solution:
    def FindGreatestSumOfSubArray(self , array ):
        # write code here
        length = len(array)
        dp = [0]*(length+1)
        dp[0] = 0
        sum_ = 0
        ret = array[0]
        temp_idx, temp_len = 0,0
        max_idx, max_len = 0,0
        for i in range(1,length+1):
            if array[i-1]> sum_+array[i-1]:   #这个数比和加这个数要大，就从这个数开始计算
                sum_ = array[i-1]
                temp_idx =i-1
                temp_len =1
            else:
                sum_ = sum_+array[i-1] #加起来大的话，就长度加1
                temp_len+=1
# 如果ret大于sum，回到之前等于的时候获取到的最大值就可以 #如果ret<=sum 更新下max_id最大值的位置
            if ret <= sum_:
                max_len = temp_len
                max_idx = temp_idx
                ret = sum_
        return array[max_idx:max_idx+max_len]
#自己做的，厉害啦
class Solution2:
    def FindGreatestSumOfSubArray(self , array):
        # write code here
        length=len(array)
        sum=0
        ret=array[0]
        temp_id,temp_len=0,0
        max_id,max_len=0,0
        for i in range(length):
            if array[i]>(array[i]+sum):
                temp_id=i
                temp_len=1
                sum=array[i]
            else:
                sum=array[i]+sum
                temp_len+=1
            if ret<=sum:
                ret=sum
                max_id=temp_id
                max_len=temp_len
        return array[max_id:max_id+max_len]
if __name__ == '__main__':
    array=[-1,1,-3,5,-2]
    a=Solution2()
    print(a.FindGreatestSumOfSubArray(array))