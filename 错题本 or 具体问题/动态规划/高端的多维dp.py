'''
2024年8月6日22:57:07
力扣题目: https://leetcode.cn/problems/maximum-score-from-grid-operations/description/
3225. 网格图操作后的最大分数



'''


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        def maxScore(grid):
            n = len(grid)
            left_max = [[0] * n for _ in range(n)]  # 实际上可以优化为一维数组
            right_max = [[0] * n for _ in range(n)]  # 实际上可以优化为一维数组

            # 初始化right_max，从右向左，从下到上
            for j in range(n):
                max_right = 0
                for i in range(n - 1, -1, -1):
                    if grid[i][j] == 0:  # 白色格子
                        right_max[i][j] = max_right
                    else:
                        max_right = max(max_right, grid[i][j])

            # 初始化left_max，从左向右，从下到上
            for j in range(n):
                max_left = 0
                for i in range(n - 1, -1, -1):
                    if grid[i][j] == 0:
                        left_max[i][j] = max_left
                    else:
                        max_left = max(max_left, grid[i][j])

            # 计算最大分数
            max_score = 0
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 0:
                        # 如果左边或右边有黑色格子，则加上左侧或右侧的最大白色格子分数
                        max_score += max(left_max[i][j], right_max[i][j])

            return max_score

        return maxScore(grid)