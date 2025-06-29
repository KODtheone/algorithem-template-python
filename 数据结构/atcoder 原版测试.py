'''
哪位大佬帮我看看,  atcode的lazy segment tree板子, 来定义 维护sum值这样写为什么会出错?
ls = LazySegmentTree(add, 0, add, add, 0, n)

答: 对树上的一个节点做加法的时候，加的不是delta，而是delta*这个节点对应的区间长度
'''
# 最原始  2024年10月31日09:56:50
def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1
    return x


def _bsf(n: int) -> int:
    x = 0
    while n % 2 == 0:
        x += 1
        n //= 2
    return x




import typing
from operator import add

# xxx = LST(op, e, mapping, composition,  lazy_init , num)
class LazySegmentTree:
    def __init__(
            self,
            op: typing.Callable[[typing.Any, typing.Any], typing.Any],
            e: typing.Any,
            mapping: typing.Callable[[typing.Any, typing.Any], typing.Any],
            composition: typing.Callable[[typing.Any, typing.Any], typing.Any],
            id_: typing.Any,
            v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = (self._n-1).bit_length()
        self._size = 1 << self._log
        self.tree = [e] * (2 * self._size)
        self._lz = [self._id] * self._size
        for i in range(self._n):
            self.tree[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self.tree[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self.tree[p]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        if left == right:
            return self._e

        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push(right >> i)

        sml = self._e
        smr = self._e
        while left < right:
            if left & 1:
                sml = self._op(sml, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self.tree[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self.tree[1]

    def apply(self, left: int, right: typing.Optional[int] = None,
              f: typing.Optional[typing.Any] = None) -> None:
        assert f is not None

        if right is None:
            p = left
            assert 0 <= left < self._n

            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self.tree[p] = self._mapping(f, self.tree[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            assert 0 <= left <= right <= self._n
            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2

            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(
            self, left: int, g: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert g(self._e)

        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(self._op(sm, self.tree[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2
                    if g(self._op(sm, self.tree[left])):
                        sm = self._op(sm, self.tree[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self.tree[left])
            left += 1

        return self._n

    def min_left(self, right: int, g: typing.Any) -> int:
        assert 0 <= right <= self._n
        assert g(self._e)

        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self._op(self.tree[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self._op(self.tree[right], sm)):
                        sm = self._op(self.tree[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self.tree[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self.tree[k] = self._op(self.tree[2 * k], self.tree[2 * k + 1])

    def _all_apply(self, k: int, f: typing.Any) -> None:
        self.tree[k] = self._mapping(f, self.tree[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k: int) -> None:
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._id

    def __str__(self):
        return str([self.get(i) for i in range(self._n)])

n = 10
n = [0] * n
m = 50
# self_sum = LST(n, m, m, add, app, com1)
# ssum = LST(n, 0, -1, add, app, com1)
# ssum = LST(n, 0, 0, add, app, com1)
# xxx = LST(op, e, mapping, composition,  lazy_init , num)
# ssum = LST(n, 0, 0, add, add, add)  #  initlazy 必须要为0
ls = LazySegmentTree(add, 0, add, add, 0, n)
# ssum = LST(n, 0, -454, add, app, com1)
# self_max = LST(n * [m], -inf, m, max, app, com2)
# self_max = LST(n, 0, 0, max, app, com1)

# print(ls)
# print(ls.prod(0, 3))
# ls.apply(0, 3, 10)
# ls.apply(1, 4, 0)
# # ssum.update(0, 4, 4)
# print(ls)
# # print(self_sum.lazy)
# print(ls.prod(0, 0))
# print(ls.prod(0, 1))
# print(ls.prod(0, 2))
# # 线段树 sum 有问题
# print(ls.prod(0, 3))
# print(ls.prod(0, 9))
# print(ls.tree)

'''
正确的解法:  因为要维护 sum,  lst需要多维护一维,  单元的长度
'''
# 1,  set 式
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


def app(lz, a):
    return [a[1] * lz , a[1]]

def com(l1, l2):
    # if l2 == initlazy: return l1
    return l1
# s = LST(nums, initval, initlazy, op, app, com)

'''
2024年9月29日09:26:56  模版使用问题, sum,  set 形
'''

def op(a1, a2):
    return [a1[0] + a2[0] , a1[1] + a2[1]]

n = 10
# n = [0] * n
m = 50
# self_sum = LST(n, m, m, add, app, com1)
# ssum = LST(n, 0, -1, add, app, com1)
# ssum = LST(n, 0, 0, add, app, com1)
ssum = LST(10 * [[0, 1]], [0,0], 0, op, app, com)  #  initlazy = 0  意味着, 断更新时 不能更新成0  不然出错 ,  可以
ssum = LST(10 * [[0, 1]], [0,0], "不会选到的东西", op, app, com)  #  initlazy = 0  意味着, 断更新时 不能更新成0  不然出错 ,  可以初始成不会选到的东西
# ssum = LST(n, 0, -454, add, app, com1)
# self_max = LST(n * [m], -inf, m, max, app, com2)
# self_max = LST(n, 0, 0, max, app, com1)

print("ssum", ssum,  )
print(ssum.query(0, 3))
ssum.update(0, 3, 10)   # set式
ssum.update(3, 4, 2)
ssum.update(0, 4, 4)
print("ssum", ssum)
# print(self_sum.lazy)
print(ssum.query(0, 0))
print(ssum.query(0, 1))
print(ssum.query(0, 2))
# 线段树 sum 有问题
print(ssum.query(0, 3))
print(ssum.query(0, 4))
print(ssum.query(0, 5))
print(ssum.query(0, 9))
print("ssum.tree", ssum.tree)

# 2,  sum  add式修改:
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
    return [a1[0] + a2[0] , a1[1] + a2[1]]
def app(lz, a):
    return [a[0] + a[1] * lz , a[1]]

def com(l1, l2):
    # if l2 == initlazy: return l1
    return l1 + l2
# s = LST(nums, initval, initlazy, op, app, com)

n = 10
# n = [0] * n
m = 50
# self_sum = LST(n, m, m, add, app, com1)
# ssum = LST(n, 0, -1, add, app, com1)
# ssum = LST(n, 0, 0, add, app, com1)
ssum = LST(10 * [[0, 1]], [0,0], 0, op, app, com)  #  initlazy 必须要为0
# ssum = LST(n, 0, -454, add, app, com1)
# self_max = LST(n * [m], -inf, m, max, app, com2)
# self_max = LST(n, 0, 0, max, app, com1)

print("ssum", ssum,  )
print(ssum.query(0, 3))
ssum.update(0, 3, 10)   # set式
ssum.update(3, 4, 2)
ssum.update(0, 4, 4)
# ssum.set(0, [3,33])
print("ssum", ssum)
# print(self_sum.lazy)
print(ssum.query(0, 0))
print(ssum.query(0, 1))
print(ssum.query(0, 2))
# 线段树 sum 有问题
print(ssum.query(0, 3))
print(ssum.query(0, 4))
print(ssum.query(0, 5))
print(ssum.query(0, 9))
print("ssum.tree", ssum.tree)