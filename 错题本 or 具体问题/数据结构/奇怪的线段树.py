'''
2024年8月9日17:21:23  https://leetcode.cn/problems/fancy-sequence/description/  1622. 奇妙序列
似乎是经典题目
但对线段树来讲比较奇怪
我一开始有一个列表 nums = []
操作1:  append(val)
操作2:  所有nums元素 + x
操作3:  所有nums元素 * x
操作4:  查询 第i个元素

第二种数学做法, 非常简单  利用 乘法逆元 可以还原成操作前的值
方法3 , 用 numpy偷鸡...
'''

#  方法1:  很好笑,还真是怎么op都行
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

initval = 0
initlazy = (1, 0) # * 1 + 0

def op(a, b):
    return 0

def app(lz, a):
    return (a * lz[0] + lz[1]) % (10**9+7)

def com(l1, l2):
    return (l1[0] * l2[0]) % (10**9+7) , (l1[0] * l2[1] + l1[1]) % (10**9+7)

lst = LST(10**5 + 1, 0, initlazy, op, app, com)

class Fancy:

    def __init__(self):
        self.i = -1

    def append(self, val: int) -> None:
        self.i += 1
        lst.update(self.i,  self.i, (0, val))

    def addAll(self, inc: int) -> None:
        lst.update(0, self.i, (1, inc))

    def multAll(self, m: int) -> None:
        lst.update(0, self.i, (m, 0))

    def getIndex(self, idx: int) -> int:
        if idx > self.i: return -1
        return lst.get(idx) % (10**9+7)

# 方法2  数学  用乘法逆元来做除法就是非常神奇, 还不会出错...
class Fancy:

    def __init__(self):
        self.lst = []
        self.a = 1
        self.b = 0
        self.mod = 10**9+7

    def append(self, val: int) -> None:
        self.lst.append((val-self.b)*pow(self.a, -1,self.mod))

    def addAll(self, inc: int) -> None:
        self.b = (self.b+inc)%self.mod

    def multAll(self, m: int) -> None:
        self.a = self.a*m%self.mod
        self.b = self.b*m%self.mod

    def getIndex(self, idx: int) -> int:
        return (self.lst[idx]*self.a+self.b)%self.mod if idx<len(self.lst) else -1

# 方法三
import numpy as np

mod = 10**9 + 7
class Fancy:

    def __init__(self):
        self.tmp = np.array([], dtype=np.int64)

    def append(self, val: int) -> None:
        self.tmp = np.append(self.tmp, val)

    def addAll(self, inc: int) -> None:
        self.tmp += inc
        self.tmp %= mod

    def multAll(self, m: int) -> None:
        self.tmp *= m
        self.tmp %= mod

    def getIndex(self, idx: int) -> int:
        return self.tmp[idx].item() if len(self.tmp) > idx else -1

