'''
例题:https://leetcode.cn/problems/count-of-range-sum/solutions/1256482/cpython3-0er-fen-1gui-bing-pai-xu-2shu-z-9dc4/
还需要提炼一下做法.  这道题跟踪pre_sum的方法我倒是会了,但是这个利用树状数组,感觉有些绕远路了...


'''
from typing import List


class BIT:  # 树状数组 动态前缀和
    def __init__(self, n):
        self.tree = [0 for x in range(n + 1)]
        self.n = n

    # ---- 最右侧1的权重
    def lowbit(self, i: int) -> int:
        return i & (-i)

    # ----某个位置，加上k
    def update(self, i: int, k: int) -> None:
        while i <= self.n:
            self.tree[i] += k
            i += self.lowbit(i)

    # ----前缀和（实指）
    def presum(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= self.lowbit(i)
        return res


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        # ---- 前缀和 实指
        presum = [0 for _ in range(n + 1)]
        for i in range(n):  # 虚指
            presum[i + 1] = presum[i] + nums[i]
            # ------------------ 以presum 为对象  离散化 + 树状数组----------------------#
        # ------ 所有的点
        all_num = []
        for x in presum:
            all_num += [x, x - lower, x - upper]
        # print(all_num)

        # ------ 离散化
        all_num = list(set(all_num))  # 离散化，要去重 都行
        all_num.sort()  # 排序
        # print(all_num)

        val_id = dict()
        for i, x in enumerate(all_num):
            val_id[x] = i
        # ------ 树状数组
        bit = BIT(len(all_num))
        res = 0
        for i, x in enumerate(presum):  # 遍历，往前探
            idL = val_id[x - upper]
            idR = val_id[x - lower]
            res += (bit.presum(idR + 1) - bit.presum(idL + 1 - 1))

            ID = val_id[x]
            bit.update(ID + 1, 1)

        return res

