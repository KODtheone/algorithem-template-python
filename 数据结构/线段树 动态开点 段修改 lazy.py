'''
2024年7月28日09:32:36,  整理一个最强大的线段是模板吧  之前的发现还是没有断修改功能
# 主要功能就是需要 段改, 段差的, 在加上一个树上二分查找;
哦,还有动态开点, 应对 值域太大 直接爆炸的情况
例题:  https://leetcode.cn/problems/falling-squares/description/?envType=daily-question&envId=2024-07-28

段修改就以利用了lazy标志
说明见 https://leetcode.cn/circle/discuss/ROAHXD/#%E5%9F%BA%E6%9C%AC%E6%80%A7%E8%B4%A8

2024年8月8日14:42:25,  还需要  1, 查询sum 区间=x    2, 查询sum 区间 + x
最好的结果,就是搞清楚 atcoder lazy segment tree 的板子, 一步到位,可以diy用法了...
2024年8月8日22:51:13, 上面的可以用终极模板搞定了
但是, 动态开点的还不行, 似乎是离散化的思想, 也许可以加入进终极魔板

'''
from math import inf
from operator import add


#链接：https://leetcode.cn/problems/falling-squares/solutions/1518294/-by-lcbin-5rop/
# 使用:  开点  固定 l = 0, r = 1e9 ; modify 段修改, 赋值(set)型  ; query 端查询  ; max型
# type: 查询max, 区间赋值 = x
##  r给大一些,也是勉强可以的 例如1e99 但是数据上不知道有没有问题...
class Node:
    def __init__(self, l, r):
        self.left = None
        self.right = None
        self.l = l
        self.r = r
        self.mid = (l + r) >> 1
        self.v = 0
        self.add = 0    # 懒标记

class SegmentTree:
    def __init__(self):
        self.root = Node(0, int(1e9))

    def modify(self, l, r, v, node=None):
        if l > r:
            return
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            node.v = v
            node.add = v
            return
        self.pushdown(node)
        if l <= node.mid:
            self.modify(l, r, v, node.left)
        if r > node.mid:
            self.modify(l, r, v, node.right)
        self.pushup(node)

    def query(self, l, r, node=None):
        if l > r:
            return 0
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            return node.v
        self.pushdown(node)
        v = 0
        if l <= node.mid:
            v = max(v, self.query(l, r, node.left))
        if r > node.mid:
            v = max(v, self.query(l, r, node.right))
        return v

    def pushup(self, node):
        node.v = max(node.left.v, node.right.v)

    def pushdown(self, node):
        if node.left is None:
            node.left = Node(node.l, node.mid)
        if node.right is None:
            node.right = Node(node.mid + 1, node.r)
        if node.add:
            node.left.v = node.add
            node.right.v = node.add
            node.left.add = node.add
            node.right.add = node.add
            node.add = 0


'''
2024年8月7日14:30:17, acl atcoder library python 里的线段树 修改版
https://leetcode.cn/circle/discuss/ROAHXD/

pushudown 和 pushup: 下放懒惰标记可以写一个专门的函数 pushdown，从儿子节点更新当前节点也可以写一个专门的函数 maintain（或者对称地用 pushup），降低代码编写难度。

apply定义区间修改的方式；
compose定义多个区间修改叠加的方式；
initlazy表示不进行区间修改的懒标记。

#  更换 ,直接看atcoder的线段树好了, 另外, 普通模板就保留两种区间修改 1, 修改为 + x 2, set 为 x
'''

##参数 nums: 初始数组   initval: 初始值  initlazy: 初始lazy标记 0?   op: 操作  apply: 区间修改方法
## compose 区间修改叠加方法   这些都是要自己写的???
## 2024年8月8日14:23:47, 没搞定...
## 2024年8月8日21:45:09,  基本搞定了,但是还有点问题, 比如 query 出来也是二维的,而且,长度有点怪...
class LazySegmentTree:
    __slots__ = 'n', 'height', 'size', 'initval', 'initlazy', 'op', 'apply', 'compose', 'tree', 'lazy'
    def __init__(self, nums, initval, initlazy, op, apply, compose):
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
        # print(self.tree[rt])
        self.tree[rt] = self.op(self.tree[rt*2], self.tree[rt*2+1])

    def pushdown(self, rt):
        if self.lazy[rt] == self.initlazy: return  #atcoder 的写法没有这个, 因为self.initlazy进行modify,对结点val 和 结点lazytag都没有影响
        self.modify(rt*2, self.lazy[rt])    # 注意这里, val给的就是lasy[rt] 因此lazy tag 直接下方用于计算了
        self.modify(rt*2+1, self.lazy[rt])
        self.lazy[rt] = self.initlazy

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

    def modify(self, rt, val):
        self.tree[rt] = self.apply(val, self.tree[rt])
        if rt < self.size:
            self.lazy[rt] = self.compose(val, self.lazy[rt])
            1

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

    def __str__(self):    # 这个东西加入后, 会有一个,每一步都自动更新的效果, 似乎把lazy标记的功能抹消了, 所以不应该加
        return str([self.get(i) for i in range(self.n)])

# 区间修改 +x , 维护sum的线段树
def app(lz, data):
    v, s = data
    return v + lz * s, s

def com(lz1, lz2):
    return lz1 + lz2

def op(d1, d2):
    v1, s1 = d1
    v2, s2 = d2
    return v1 + v2 ,  s1 + s2
# com = lambda a , b : a
# com = lambda a , b : a
# 2024年8月7日16:45:20, 看起来是通过测试了 但是, lazy标志的应用我还是没搞清, 然后找个题实验一下吧
# 2024年8月7日16:53:23 通过了 https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-ii/description/      注意, add的话 initval 就写0 不能乱写  原理待研究
# 2024年8月7日21:44:07 区间赋值通过了, 但是区间加, 即 apply = add  没有通过
# 没通过的题: https://www.luogu.com.cn/problem/P3372


a = [6,7,8,9,10]
a = [(x,1) for x in a]
#     def __init__(self, nums, initval, initlazy, op, apply, compose):
# s = LazySegmentTree(a, (0), -99999999, add, com, com)
s = LazySegmentTree(a, (0, 0), inf, op, app, com)
# s = LazySegmentTree(a, -9999999, -99, max, apply, compose)
print(s.tree)
print(s)
print(s.query(0,0))  #长度多了2 大概是因为加上了一个空的initval 2024年8月8日21:49:41, 修改 initval后对了...
print(s.query(0,1))
print(s.query(0,2))
print(s.query(0,3))
# print(s.lazy)

# print(s.query(2,2))
# print(s.query(0,7))  # 最多只能扩充到补满2n 或者说 size
# print(s.lazy)
# s.update(1,4, -1)
# s.update(0,3, 0)
# # print(s.lazy, " lazy")
# print(s)
# print(s.get(3), "get")
# print(s.query(0,4))
# print(s)
# s.update(1,2,2)
# print(s)
# print(s.query(0,1))
# print(s.query(0,4))
# print(s.query(3,4))
# print(s.query(4,4))
# s.update(0,4, 1)    # 出问题了, 改成 全是1就出bug
# s.update(0,4, 2)
# print(s)
# print(s.tree)
# print(s.query(0,4))

# a = [3] *5
# s2 = LazySegmentTree(a, 0, inf, add, com, com)
# print(s2)
# print(s2.tree)
## 2024年8月8日12:34:48 ,确认, 懒标记传递是有问题的
