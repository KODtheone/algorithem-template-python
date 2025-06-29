'''
例题:https://leetcode.cn/problems/range-sum-query-mutable/solutions/2524481/dai-ni-fa-ming-shu-zhuang-shu-zu-fu-shu-lyfll/
一个丝滑的动画视频:https://www.bilibili.com/video/BV1ce411u7qP/?vd_source=c3405c73656cbabbc56a2be0b4a50004

基础功能:  修改元素值,  查询范围和
'''
from typing import List


# 查询固定为, 查left到right (包含right点) 的闭区间和;  update更新一个点的值
# 实际使用例子,见下面
class BIT:
    def __init__(self, nums: List[int]):
        self.n = n = len(nums)
        tree = [0] * (n + 1)
        for i, x in enumerate(nums, 1):
            tree[i] += x
            if (nxt := i + (i & -i)) <= n:
                tree[nxt] += tree[i]  # 向前滚一位提前加, 因此形成了累加;
        self.nums = nums
        self.tree = tree

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        i = index + 1
        while i < self.n + 1:
            self.tree[i], i = self.tree[i] + delta, i + (i & -i)  # += 加;也行 #注意 &的优先级低于+

    def query(self, left: int, right: int) -> int:
        return self.presum(right + 1) - self.presum(left)

    def presum(self, i: int) -> int:
        s = 0
        while i:
            s += self.tree[i]
            i &= i - 1  # 等价于 i -= i & -i;解释 i -1 相当于 i的lowbit位开始都改变(1变0,后面的0都变1)
        return s


# 使用例子
a = [1, 5, 6, 9, 8, 7, 8, 0, 2, -8, 5, 6, 4]
nx = BIT(a)
print(nx.nums)
nx.update(2, 99)
print(nx.nums)
c = nx.query(2, 10)
print(c)
# 特例尝试 :  区间为0
c = nx.query(0, -1)  # right = -1 成功
print(c)
c = nx.query(3, 2)
print(c)

#纯享版
class Bit:
    def __init__(self, nums: List[int]):
        self.n = n = len(nums)
        tree = [0] * (n + 1)
        for i, x in enumerate(nums, 1):
            tree[i] += x
            if (nxt := i + (i & -i)) <= n:
                tree[nxt] += tree[i]
        self.nums = nums
        self.tree = tree

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        i = index + 1
        while i < self.n + 1:
            self.tree[i], i = self.tree[i] + delta, i + (i & -i)

    def query(self, left: int, right: int) -> int:
        return self.presum(right + 1) - self.presum(left)

    def presum(self, i: int) -> int:
        s = 0
        while i:
            s += self.tree[i]
            i &= i - 1
        return s

