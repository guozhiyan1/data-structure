"""
输入一个非负整数数组numbers，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组[3，32，321]，则打印出这三个数字能排成的最小数字为321323。
1.输出结果可能非常大，所以你需要返回一个字符串而不是整数
2.拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
"""
#法一，重新定义排序（重载比较的排序）： 组成数字最小来排序  3和32组成332和323,323小所以32小于3 同理321小于32    321<32<3 从小打大排序得出数组

import functools
class Solution:
    def PrintMinNumber(self , numbers) -> str:
        #空数组的情况
        if not numbers:
            return ""
        #将数字转成字符
        nums = list(map(str, numbers))
        #重载比较大小
        cmp = lambda a, b: 1 if a + b > b + a else -1
        #排序
        nums.sort(key = functools.cmp_to_key(cmp))
        #字符串叠加  "['11', '3']"  列表转字符串
        return "".join(nums)
#法二，比较排序
class Solution:
    def PrintMinNumber(self , numbers: List[int]) -> str:
        # write code
        if not numbers:
            return ""
        l=len(numbers)
        for i in range(l-1):
            for j in range(i+1,l):
                if str(numbers[i])+str(numbers[j])>str(numbers[j])+str(numbers[i]):
                    numbers[i],numbers[j]=numbers[j],numbers[i]
        print(numbers)
        numbers=list(map(str,numbers))
        return "".join(numbers)
"""
贪心算法：当前看起来最优解，只看眼前   问题可以分成子问题（分而知之），子问题最优解能递推到最终问题的最优解。 动态规划可以回退，保存所有的结果（贪心只保持最优解）
不太能解决生活中的大部分问题   这道题不算严格意义上贪心算法
"""