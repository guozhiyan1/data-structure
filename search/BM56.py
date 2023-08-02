"""
知识点：递归与回溯

"""
class Solution:
    def recursion(self, res, num, temp, vis):
        # 临时数组满了加入输出
        if len(temp) == len(num):
            res.append(temp.copy())
            return
        # 遍历所有元素选取一个加入
        for i in range(len(num)):
            # 如果该元素已经被加入了则不需要再加入了
            if vis[i] == 1:
                continue
            if i > 0 and num[i - 1] == num[i] and not vis[i - 1]:
                # 当前的元素num[i]与同一层的前一个元素num[i-1]相同且num[i-1]已经用过了
                continue
                # 标记为使用过
            vis[i] = 1
            # 加入数组
            temp.append(num[i])
            self.recursion(res, num, temp, vis)
            # 回溯
            vis[i] = 0
            temp.pop()

    def permuteUnique(self, num):
        # 先按字典序排序
        num.sort()
        # 标记每个位置的元素是否被使用过
        vis = [0] * len(num)
        res = list(list())
        temp = list()
        # 递归获取
        self.recursion(res, num, temp, vis)
        return res

if __name__ == '__main__':
    a=Solution()
    print(a.permuteUnique([2,2,3]))