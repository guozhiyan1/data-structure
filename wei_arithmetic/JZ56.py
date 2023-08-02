class Solution:
    def FindNumsAppearOnce(self , array: List[int]) -> List[int]:
        # write code here
        a=[]
        for i in range(len(array)):
            if array.count(array[i])==1:
                a.append(array[i])
        a.sort()
        return a
"""
数组中只出现一次的两个数字
法2：
1、创建一个哈希表
2、当数组元素没有在哈希表中成为key的时候，put进哈希表，当已存在的时候，则remove掉。
3、最后哈希表中剩下的key就是只出现一次的数字
4、遍历key然后返回结果
"""
class Solution:
    def FindNumsAppearOnce(self , array: List[int]) -> List[int]:
        # write code here
        a={}
        b=[]
        for i in range(len(array)):
            if array[i] not in a:
                a[array[i]]=i
            else:
                a.pop(array[i])
        for key in a:
            b .append(key)
        return sorted(b)

"""
法三，位运算
step 1：遍历整个数组，将每个元素逐个异或运算，。
step 2：我们可以考虑位运算的性质，找到二进制中第一个不相同的位，将所有数组划分成两组。
step 3：遍历数组对分开的数组单独作异或连算。
step 4：最后整理次序输出。
kanbudong
"""
class Solution:
    def FindNumsAppearOnce(self , array):
        res = [0, 0]
        temp = 0
        #遍历数组得到a^b
        for i in range(len(array)):
            temp ^= array[i]
        k = 1
        #找到两个数不相同的第一位
        while k & temp == 0:
            k <<= 1
        for i in range(len(array)):
            #遍历数组，对每个数分类
            if k & array[i] == 0 :
                res[0] ^= array[i]
            else:
                res[1] ^= array[i]
        #整理次序
        res.sort()
        return res