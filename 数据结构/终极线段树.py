'''
2024年8月8日21:50:28, 线段树的终极板子
主要来自 atcoder 的 lazy segtree python 模板
FatalError 修改后的板子  https://leetcode.cn/circle/discuss/ROAHXD/
LazySegmentTree

2024年9月29日03:45:34,  使用例子: https://leetcode.cn/problems/booking-concert-tickets-in-groups/ 的提交
2024年9月29日09:16:01, sum的使用 感觉还有问题...   见最下面.  ### 注意!!!
2024年10月19日22:21:14  试试原版  atcode 的   https://github.com/not522/ac-library-python/blob/master/atcoder/lazysegtree.py

2024年10月31日10:27:44,  一个优秀使用例子 https://leetcode.cn/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/
见其中的笔记和 备注     3165. 不包含相邻元素的子序列的最大和   此题相当于,把打家劫舍的结果值 线段树化保存
'''
from operator import add


# nums 需要处理成 多维形式  根据 initval的维度; app: lazy tag 对 结点val的操作 com: 两个lazy tag 的合并
# app: (lazy, node) -> node    com: (lazy1, lazy2) -> lazy (lazy1 新来的)
class LST:
    __slots__ = 'n', 'height', 'size', 'initval', 'initlazy', 'op', 'apply', 'compose', 'tree', 'lazy'
    def __init__(self, nums, initval, initlazy, op, apply, compose):
        if isinstance(nums, int):
            nums = [initval] * nums
        self.n = len(nums)
        self.height = (self.n-1).bit_length()
        self.size = 1 << self.height
        self.initval = initval
        self.initlazy = initlazy
        self.op = op
        self.apply = apply
        self.compose = compose
        self.tree = [initval for _ in range(2 * self.size)]
        self.tree[self.size:self.size+self.n] = nums
        for i in range(self.size-1, 0, -1):
            self.pushup(i)
        self.lazy = [initlazy for _ in range(self.size)]

    def pushup(self, rt):
        self.tree[rt] = self.op(self.tree[rt*2], self.tree[rt*2+1])

    def pushdown(self, rt):
        if self.lazy[rt] == self.initlazy: return  ##
        self.modify(rt*2, self.lazy[rt])
        self.modify(rt*2+1, self.lazy[rt])
        self.lazy[rt] = self.initlazy

    def modify(self, rt, val):
        self.tree[rt] = self.apply(val, self.tree[rt])
        if rt < self.size:
            self.lazy[rt] = self.compose(val, self.lazy[rt])

    def set(self, idx, val):
        idx += self.size
        for i in range(self.height, 0, -1):
            self.pushdown(idx >> i)
        self.tree[idx] = val
        for i in range(1, self.height + 1):
            self.pushup(idx >> i)

    def update(self, left, right, val):
        if left > right: return
        left += self.size
        right += self.size
        for i in range(self.height, 0, -1):
            if left >> i << i != left:
                self.pushdown(left >> i)
            if (right+1) >> i << i != right+1:
                self.pushdown(right >> i)
        l, r = left, right
        while left <= right:
            if left & 1:
                self.modify(left, val)
                left += 1
            if not right & 1:
                self.modify(right, val)
                right -= 1
            left >>= 1
            right >>= 1
        left, right = l, r
        for i in range(1, self.height + 1):
            if left >> i << i != left:
                self.pushup(left >> i)
            if (right+1) >> i << i != right+1:
                self.pushup(right >> i)

    def get(self, idx):
        idx += self.size
        for i in range(self.height, 0, -1):
            self.pushdown(idx >> i)
        return self.tree[idx]

    def query(self, left, right):
        if left > right: return self.initval
        left += self.size
        right += self.size
        for i in range(self.height, 0, -1):
            if left >> i << i != left:
                self.pushdown(left >> i)
            if (right+1) >> i << i != right+1:
                self.pushdown(right >> i)
        lres, rres = self.initval, self.initval
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
        lres = self.initval
        for i in range(self.height, 0, -1):
            self.pushdown(left >> i)

        while True:
            while not left & 1:
                left >>= 1
            if f(self.op(lres, self.tree[left])):
                while left < self.size:
                    self.pushdown(left)
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
        rres = self.initval
        for i in range(self.height, 0, -1):
            self.pushdown(right >> i)

        while True:
            while right > 1 and right & 1:
                right >>= 1
            if f(self.op(self.tree[right], rres)):
                while right < self.size:
                    self.pushdown(right)
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


# 2024年8月9日16:58:59, 下面com策略暂时是对的
# 区间赋值的 com  在有 if self.lazy[rt] == self.initlazy: return的情况
def com(l1, l2):
    return l1

# 不然
def com(l1, l2):
    if l1 == initlazy: return l2
    return l1

# 2024年8月21日14:47:55
## 纯享版
class LST:
    __slots__ = 'n', 'height', 'size', 'initval', 'initlazy', 'op', 'apply', 'compose', 'tree', 'lazy'
    def __init__(self, nums, initval, initlazy, op, apply, compose):
        if isinstance(nums, int):
            nums = [initval] * nums
        self.n = len(nums)
        self.height = (self.n-1).bit_length()
        self.size = 1 << self.height
        self.initval = initval
        self.initlazy = initlazy
        self.op = op
        self.apply = apply
        self.compose = compose
        self.tree = [initval for _ in range(2 * self.size)]
        self.tree[self.size:self.size+self.n] = nums
        for i in range(self.size-1, 0, -1):
            self.pushup(i)
        self.lazy = [initlazy for _ in range(self.size)]

    def pushup(self, rt):
        self.tree[rt] = self.op(self.tree[rt*2], self.tree[rt*2+1])

    def pushdown(self, rt):
        if self.lazy[rt] == self.initlazy: return  ##
        self.modify(rt*2, self.lazy[rt])
        self.modify(rt*2+1, self.lazy[rt])
        self.lazy[rt] = self.initlazy

    def modify(self, rt, val):
        self.tree[rt] = self.apply(val, self.tree[rt])
        if rt < self.size:
            self.lazy[rt] = self.compose(val, self.lazy[rt])

    def set(self, idx, val):
        idx += self.size
        for i in range(self.height, 0, -1):
            self.pushdown(idx >> i)
        self.tree[idx] = val
        for i in range(1, self.height + 1):
            self.pushup(idx >> i)

    def update(self, left, right, val):
        if left > right: return
        left += self.size
        right += self.size
        for i in range(self.height, 0, -1):
            if left >> i << i != left:
                self.pushdown(left >> i)
            if (right+1) >> i << i != right+1:
                self.pushdown(right >> i)
        l, r = left, right
        while left <= right:
            if left & 1:
                self.modify(left, val)
                left += 1
            if not right & 1:
                self.modify(right, val)
                right -= 1
            left >>= 1
            right >>= 1
        left, right = l, r
        for i in range(1, self.height + 1):
            if left >> i << i != left:
                self.pushup(left >> i)
            if (right+1) >> i << i != right+1:
                self.pushup(right >> i)

    def get(self, idx):
        idx += self.size
        for i in range(self.height, 0, -1):
            self.pushdown(idx >> i)
        return self.tree[idx]

    def query(self, left, right):
        if left > right: return self.initval
        left += self.size
        right += self.size
        for i in range(self.height, 0, -1):
            if left >> i << i != left:
                self.pushdown(left >> i)
            if (right+1) >> i << i != right+1:
                self.pushdown(right >> i)
        lres, rres = self.initval, self.initval
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
        left += self.size
        lres = self.initval
        for i in range(self.height, 0, -1):
            self.pushdown(left >> i)

        while True:
            while not left & 1:
                left >>= 1
            if f(self.op(lres, self.tree[left])):
                while left < self.size:
                    self.pushdown(left)
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
        right += self.size
        rres = self.initval
        for i in range(self.height, 0, -1):
            self.pushdown(right >> i)

        while True:
            while right > 1 and right & 1:
                right >>= 1
            if f(self.op(self.tree[right], rres)):
                while right < self.size:
                    self.pushdown(right)
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

initval, initlazy = 0, -1

def op(a1, a2):
    return

def app(lz, a):
    return

def com(l1, l2):
    if l2 == initlazy: return l1
    return
# s = LST(nums, initval, initlazy, op, app, com)



'''
2024年9月29日09:26:56  模版使用问题, sum,  set 形

'''
def app(lz, a):
    return lz

def com1(l1, l2):
    return l1

def add(a1, a2):
    return a1 + a2

n = 10
n = [0] * n
m = 50
# self_sum = LST(n, m, m, add, app, com1)
# ssum = LST(n, 0, -1, add, app, com1)
# ssum = LST(n, 0, 0, add, app, com1)
ssum = LST(n, 0, 0, add, add, add)  #  initlazy 必须要为0
# ssum = LST(n, 0, -454, add, app, com1)
# self_max = LST(n * [m], -inf, m, max, app, com2)
# self_max = LST(n, 0, 0, max, app, com1)

print(ssum)
print(ssum.query(0, 3))
ssum.update(0, 3, 10)
ssum.update(3, 4, 2)
ssum.update(0, 4, 4)
# ssum.update(1, 4, 0)   #  bug修补方式  不知道为什么, 加上这个假更新 就好了...
print(ssum)
# print(self_sum.lazy)
print(ssum.query(0, 0))
print(ssum.query(0, 1))
print(ssum.query(0, 2))
# 线段树 sum 有问题
print(ssum.query(0, 3))
print(ssum.query(0, 9))
print(ssum.tree)













