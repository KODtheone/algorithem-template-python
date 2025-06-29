'''
2024年6月8日13:56:07, 重写一个 0x3f常用形式的线段树, 以后在看题解的时候也方便
另外,也是统一我使用的线段树写法, 自己背一下板子
2024年6月8日15:53:12,优化之后, 那些三个固定参数不用写了, 使用起来也只需要写两个参量, 跟树状数组一样了

'''
from math import inf
from operator import *
from typing import List
## 注意, 如果是提前给好了 nums 使用 build 初始化st比 遍历nums, update每个值, 更加快速
# 进化模板:  init()参数可以是 int, 也可以是List[int], 如果是list,就会自己完成build

# 问题描述: 给出一个len = n 的数组nums(初始都是0, 若给了nums,则enumerate并修改值) 需要两种操作:1, 修改index上的值  2,查询[l,r]区间内的最大值
# 纯享版  以sum为例:
# 参数 单走一个n 需要计算的st的总长度
class SegmentTree:
    def __init__(self, n):
        if isinstance(n, int):
            self.n = n
            self.x = [0] * (t := 2 << n.bit_length())
        else:
            self.n = len(n)
            self.x = [0] * (2 << self.n.bit_length())
            self.build(n, 0, 0, self.n - 1)

    def build(self, nums: List[int], node: int, s: int, e: int):
        if s == e:
            self.x[node] = nums[s]
            return
        m = s + (e - s) // 2
        self.build(nums, node * 2 + 1, s, m)
        self.build(nums, node * 2 + 2, m + 1, e)
        self.x[node] = self.x[node * 2 + 1] + self.x[node * 2 + 2]

    def update(self, index: int, val: int, node = 0, s = 0, e ="e"):
        if e == "e": e = self.n - 1
        if s == e:
            self.x[node] = val
            return
        m = s + (e - s) // 2
        if index <= m: self.update(index, val, node * 2 + 1, s, m)
        else:          self.update(index, val, node * 2 + 2, m + 1, e)
        self.x[node] = self.x[node * 2 + 1] + self.x[node * 2 + 2]

    def query(self, left: int, right: int, node = 0, s = 0, e = "e") -> int:
        if e == "e": e = self.n - 1
        if left <= s and right >= e:     return self.x[node]
        x = 0
        m = s + (e - s) // 2
        if right > m:   x += self.query(left, right, node * 2 + 2, m + 1, e)
        if left <= m:   x += self.query(left, right, node * 2 + 1, s, m)
        return x

##   修改为 max
    # def query(self, left: int, right: int, node = 0, s = 0, e = "e") -> int:
    #     if e == "e": e = self.n - 1
    #     if left <= s and right >= e:     return self.x[node]
    #     mx = - inf
    #     m = s + (e - s) // 2
    #     if right > m:   mx = max(mx, self.query(left, right, node * 2 + 2, m + 1, e))
    #     if left <= m:   mx = max(mx, self.query(left, right, node * 2 + 1, s, m))
    #     return mx
    # 另外把 change中的更新点编程max

# nums = [1,2,3,4,5,6,7]
# e = len(nums) - 1
# st = SegmentTree(len(nums))   # 实例化
# for i, x in enumerate(nums):  # 相当于之前的build 录入数组
#     st.update(i, x)
# # st = SegmentTree(nums)
# print(st.x)
# print(st.query(0, 3))    # 0, 0 , e 是半固定值, 固定的递归入口,但是递归时值就变化了
# st.update(0, -2)
# print(st.query(-99, 2))
# print(st.query(0, 2))
# print(st.query(0, 0))
# # print(st.query(0, -1))
# print(st.query(4, 999))
# print(st.query(4, 6))
# # print(st.query(2, 999))
# print(st.query(2, 999))


'''max 型   '''
class SegmentTree:
    def __init__(self, n):
        if isinstance(n, int):
            self.n = n
            self.x = [0] * (t := 2 << n.bit_length())
        else:
            self.n = len(n)
            self.x = [0] * (2 << self.n.bit_length())
            self.build(n, 0, 0, self.n - 1)

    def build(self, nums: List[int], node: int, s: int, e: int):
        if s == e:
            self.x[node] = nums[s]
            return
        m = s + (e - s) // 2
        self.build(nums, node * 2 + 1, s, m)
        self.build(nums, node * 2 + 2, m + 1, e)
        self.x[node] = max(self.x[node * 2 + 1], self.x[node * 2 + 2])

    def update(self, index: int, val: int, node = 0, s = 0, e ="e"):
        if e == "e": e = self.n - 1
        if s == e:
            self.x[node] = val
            return
        m = s + (e - s) // 2
        if index <= m: self.update(index, val, node * 2 + 1, s, m)
        else:          self.update(index, val, node * 2 + 2, m + 1, e)
        self.x[node] = max(self.x[node * 2 + 1], self.x[node * 2 + 2])

    def query(self, left: int, right: int, node = 0, s = 0, e = "e") -> int:
        if e == "e": e = self.n - 1
        if left <= s and right >= e:     return self.x[node]
        x = -inf
        m = s + (e - s) // 2
        if right > m:   x = max(x, self.query(left, right, node * 2 + 2, m + 1, e))
        if left <= m:   x = max(x, self.query(left, right, node * 2 + 1, s, m))
        return x


''''
2024年8月7日14:42:47
来自 https://leetcode.cn/circle/discuss/ROAHXD/

据说这个是 zkw线段树  出处：清华大学 张昆玮(zkw) - ppt 《统计的力量》
'''
## 可以使用的 操作op 需要满足的性质:  运算满足结合律，即(a∘b)∘c=a∘(b∘c); 所以 sub不满足
## 存在单位元id, 即a∘id = id∘a = a
## 因此 ixor,  iand (需要intial = -1 作为单位元), ior也可以
## 另外,有的时候需要自己写op
## 参数说明: nums: 输入数组 initial: 初始值    op: min, max, add 等操作
class ST:
    __slots__ = 'n', 'height', 'size', 'initial', 'op', 'tree'
    def __init__(self, nums, initial=0, op=int.__add__):
        if isinstance(nums, int):
            nums = [initial] * nums
        self.n = len(nums)
        self.height = (self.n-1).bit_length()
        self.size = 1 << self.height
        self.initial = initial
        self.op = op
        self.tree = [initial for _ in range(2 * self.size)]
        self.tree[self.size:self.size+self.n] = nums
        for idx in range(self.size-1, 0, -1):
            self.pushup(idx)

    def get(self, idx):
        return self.tree[idx + self.size]

    def pushup(self, rt):
        self.tree[rt] = self.op(self.tree[rt*2], self.tree[rt*2+1])

    def update(self, idx, val):
        idx += self.size
        self.tree[idx] = val
        for i in range(1, self.height + 1):
            self.pushup(idx >> i)

    def query(self, left, right):
        # 闭区间 [left, right]
        left += self.size
        right += self.size
        lres, rres = self.initial, self.initial
        while left <= right:
            if left & 1:
                lres = self.op(lres, self.tree[left])
                left += 1
            if not right & 1:
                rres = self.op(self.tree[right], rres)
                right -= 1
            left >>= 1
            right >>= 1
        return self.op(lres, rres)

    def all(self):
        return self.tree[1]

    def bisect_left(self, left, f):
        # 查找 left 右侧首个满足 f(query(left, idx)) 为真的下标
        left += self.size
        lres = self.initial

        while True:
            while not left & 1:
                left >>= 1
            if f(self.op(lres, self.tree[left])):
                while left < self.size:
                    left *= 2
                    if not f(self.op(lres, self.tree[left])):
                        lres = self.op(lres, self.tree[left])
                        left += 1
                return left - self.size
            if left & (left + 1) == 0:
                return self.n
            lres = self.op(lres, self.tree[left])
            left += 1

    def bisect_right(self, right, f):
        # 查找 right 左侧首个满足 f(query(idx, right)) 为真的下标
        right += self.size
        rres = self.initial

        while True:
            while right > 1 and right & 1:
                right >>= 1
            if f(self.op(self.tree[right], rres)):
                while right < self.size:
                    right = 2 * right + 1
                    if not f(self.op(self.tree[right], rres)):
                        rres = self.op(self.tree[right], rres)
                        right -= 1
                return right - self.size
            if right & (right - 1) == 0:
                return -1
            rres = self.op(self.tree[right], rres)
            right -= 1

    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


a = [1,1,1,1,1]
s = ST(a, 0, ior)
print(s.tree)
print(s)
print(s.query(2,2))
print(s.query(0,5))
s.update(0,8)
s.update(1,2)
print(s)
print(s.query(0,1))
print(s.query(0,4))
s.update(0,0)
print(s.query(0,4))