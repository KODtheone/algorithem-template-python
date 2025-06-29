#来自于蓝桥的题目  偶尔也会遇到...  https://www.lanqiao.cn/problems/17002/learning/?contest_id=174
from collections import deque
from typing import List

# 二维前缀和 纯享版
# 功能 & 参数:  生成 给入一个矩阵mat   查询 使用闭区间查询, 返回r1 c1 到 r2 c2 (闭区间点)形成的矩形中的和值
class Ms:
    def __init__(self, mat):
        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x
        self.s = s

    def query(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.s[r2 + 1][c2 + 1] - self.s[r2 + 1][c1] - self.s[r1][c2 + 1] + self.s[r1][c1]


#二维前缀和  0x3f的板子
class MatrixSum:
    def __init__(self, matrix): #matrix直接给二维列表就行
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x
        self.s = s

    # 返回左上角在 (r1,c1) 右下角在 (r2-1,c2-1) 的子矩阵元素和（类似前缀和的左闭右开）
    def query(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.s[r2][c2] - self.s[r2][c1] - self.s[r1][c2] + self.s[r1][c1]

    # 如果你不习惯左闭右开，也可以这样写
    # 返回左上角在 (r1,c1) 右下角在 (r2,c2) 的子矩阵元素和
    def query2(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.s[r2 + 1][c2 + 1] - self.s[r2 + 1][c1] - self.s[r1][c2 + 1] + self.s[r1][c1]




##  二维区间的最大值, 同滑动列表, 先横着做,再竖着做就可以了; 2024年6月26日17:28:38, 感觉泛用性不高..
# 参数 & 功能: 配合下面的代码使用, nums是从矩阵取出的一行或者一列.  k是窗口大小
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    q = deque()
    ans = []
    for i in range(len(nums)):
        if i == 0:
            q += i,
        else:
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q += i,
        if i - q[0] == k:
            q.popleft()
        if i > k - 2:
            ans += nums[q[0]],
    return ans
#跟踪最小值, 我当时选了最不用动脑子的转换:  变成负的,结果再变回来
def minS(nums: List[int], k: int) -> List[int]:
    nums = [-x for x in nums]
    q = deque()
    ans = []
    for i in range(len(nums)):
        if i == 0:
            q += i,
        else:
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q += i,
        if i - q[0] == k:
            q.popleft()
        if i > k - 2:
            ans += nums[q[0]],
    return [-x for x in ans]

#二维滑动; 先横再竖就完事了  mat是输入的matrix, nn, mm是窗口大小
tem1 = []
for xx in mat:
    tem1 += [maxSlidingWindow(xx, nn)]
box = list(zip(*tem1))  # 旋转
tem2 = []
for xx in box:
    tem2 += [maxSlidingWindow(xx, mm)]
ok = list(zip(*tem2))