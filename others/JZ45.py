import functools
class Solution:
    def PrintMinNumber(self , numbers: List[int]) -> str:
        #空数组的情况
        if not numbers:
            return ""
        #将数字转成字符
        nums = list(map(str, numbers))
        #重载比较大小
        cmp = lambda a, b: 1 if a + b > b + a else -1
        #排序
        nums.sort(key = functools.cmp_to_key(cmp))
        #字符串叠加
        return "".join(nums)
