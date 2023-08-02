"""


"""


class Solution:
    def __init__(self):
        self.count = 0

    def movingCount(self, threshold: int, rows: int, cols: int):
        flag = [[False for i in range(cols)] for j in range(rows)]
        #         for i in range(rows):
        #             for j in range(cols):
        i = 0
        j = 0
        self.dfs(threshold, rows, cols, i, j, flag)
        return self.count

    def dfs(self, threshold, rows, cols, i, j, flag):
        if i < rows and i >= 0 and j < cols and j >= 0 and (
                threshold >= i // 10 + i % 10 and threshold >= j // 10 + j % 10 and threshold >= j // 10 + j % 10 + i // 10 + i % 10) and not \
        flag[i][j]:  # threshold
            self.count += 1
            flag[i][j] = True
            self.dfs(threshold, rows, cols, i + 1, j, flag) or self.dfs(threshold, rows, cols, i - 1, j,
                                                                        flag) or self.dfs(threshold, rows, cols, i,
                                                                                          j + 1, flag) or self.dfs(
                threshold, rows, cols, i, j - 1, flag)

