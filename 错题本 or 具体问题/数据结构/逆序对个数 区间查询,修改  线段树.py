'''
2024年8月9日14:23:32, 终极逆序对问题 来源, 做 https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
还有学习 线段树 之后的思考
下面这个答案来自 g for g, 用了线段树 但没有 lazy tag
标注的 O是 Time Complexity: O(n + q*logn)   但是我总感觉应该更对 因为在算merge ,相当于 op的时候,
哦, 好像没毛病 利用前缀和计算逆序对个数  只range(n) 一重循环 , 应该是 O(n)
# 如果让我用 超级线段树模板来修改 :  initval 用这个元  Item ,  op 用 marge  , app, lazy 到 node, 用修改k值来修改node
com 用覆盖形式  ok, 似乎可以转化, 还给加上了lazy tag优化
## 我发现了 !  这题没用lazy 就是因为 ,修改是单点修改,  所以也用不着lazy更新...
那我还是自己写一个终极版

2024年8月9日15:54:32, 区间赋值还是有bug
'''

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
        return str([[self.get(i).freq] for i in range(self.n)])


class Item:
    def __init__(self, maxV):
        self.invCnt = 0
        self.freq = [0] * maxV
        self.len = 0

m = 10
initval = Item(m)   # 50 为 nums中最大值+1  根据题意来; 由于每个数据元都带一个长为m的数组,所以确实不大 ps: n为nums的长度
initlazy = 114514   # 大于m  取不到就行
def op(n1, n2):
    nn = Item(m)
    # print(n1, n2)
    nn.invCnt = n1.invCnt + n2.invCnt
    nn.len = n1.len + n2.len
    prev = [0] * m
    prev[0] = n2.freq[0]
    for i in range(m):
        nn.freq[i] = n1.freq[i] + n2.freq[i]
        if i != 0:
            nn.invCnt += n1.freq[i] * prev[i - 1]
            prev[i] = prev[i - 1] + n2.freq[i]
    return nn

def app(lz, n1):
    if lz == initlazy:
        return n1
    nn = Item(m)
    nn.freq[lz] = n1.len
    nn.invCnt = 0
    nn.len = n1.len
    return nn

def com(l1, l2):
    return l1
    if l1 == initlazy: return l2
    # if l2 == initlazy: return l1
    return l1

def main():
    arr = [1, 2, 3, 6, 5, 4]
    queries = [
        [1, 1, 3],
        [1, 2, 5],
        # [2, 2, 4, 8],
        [2, 2, 3, 7],
        [2, 2, 2, 8],
        [1, 2, 4],
        [2, 1, 4, 0],
        [2, 1, 4, 1],
        [2, 1, 4, 2],
        [2, 1, 4, 1],
        # [2, 1, 4, 3],
        [1, 1, 6]


    ]
    def f(a, l = 1)->Item:
        res = Item(m)
        res.freq[a] = l
        res.len = l
        return res

    a = [f(a) for a in arr]
    st = LST(a, initval, initlazy, op, app, com)
    print(st)
    for query in queries:
        type, *q = query
        if type == 1:
            l , r = q
            l -= 1
            r -= 1
            print(st.query(l, r).invCnt)
        elif type == 2:
            l,r,v = q
            l -= 1
            r -= 1
            # st.set(l, f(v))
            # st.update(l, r, f(v))
            st.update(l, r, v)
    print(st)
main()

# 2024年8月9日14:31:40, 原程序  查询区间逆序对数 ,  修改单点
# 功能见下面的使用例子
class SegTree:
    def __init__(self, arrVal):
        self.NEUTRAL = Item(45)
        self.n = len(arrVal)
        self.arr = arrVal
        # Empty seg
        self.seg = [Item(45) for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1)

    def merge(self, left, right):
        parent = Item(len(left.freq))
        # avoids overflow
        parent.invCnt = left.invCnt + right.invCnt
        prev = [0] * len(left.freq)
        prev[0] = right.freq[0]
        for i in range(len(left.freq)):
            parent.freq[i] = left.freq[i] + right.freq[i]
            if i != 0:
                parent.invCnt += 1 * left.freq[i] * prev[i - 1]
                prev[i] = prev[i - 1] + right.freq[i]
        return parent

    def build(self, p, l, r):
        if l == r:
            self.seg[p].invCnt = 0
            self.seg[p].freq[self.arr[l]] = 1
            return self.seg[p]
        m = (l + r) // 2
        self.seg[p] = self.merge(self.build(2 * p, l, m), self.build(2 * p + 1, m + 1, r))
        return self.seg[p]

    def build_tree(self):
        return self.build(1, 0, self.n - 1)

    def set(self, i, v, p, l, r):
        if i < l or i > r:
            return self.seg[p]
        if l == r:
            self.seg[p].freq[self.arr[i]] = 0
            self.seg[p].freq[v] = 1
            self.arr[i] = v
            return self.seg[p]
        m = (l + r) // 2
        self.seg[p] = self.merge(self.set(i, v, 2 * p, l, m), self.set(i, v, 2 * p + 1, m + 1, r))
        return self.seg[p]

    def set_value(self, i, v):
        return self.set(i, v, 1, 0, self.n - 1)

    def query(self, lx, rx, p, l, r):
        if lx > r or l > rx:
            return self.NEUTRAL
        if lx <= l and r <= rx:
            return self.seg[p]
        m = (l + r) // 2
        return self.merge(self.query(lx, rx, 2 * p, l, m), self.query(lx, rx, 2 * p + 1, m + 1, r))

    def query_range(self, lx, rx):
        return self.query(lx, rx, 1, 0, self.n - 1).invCnt


class Item:
    def __init__(self, maxV):
        self.invCnt = 0
        self.freq = [0] * maxV


def main():
    arr = [1, 2, 3, 6, 5, 4]
    queries = [
        [1, 1, 3],
        [1, 2, 5],
        [2, 2, 8],
        [2, 3, 7],
        # [2, 4, 8],
        [1, 1, 4]
    ]

    st = SegTree(arr)

    for query in queries:
        type = query[0]
        if type == 1:
            l = query[1] - 1  # Making Zero based indexing
            r = query[2] - 1  # Making Zero based indexing
            print(st.query_range(l, r))
        elif type == 2:
            i = query[1] - 1  # Making Zero based indexing
            v = query[2]
            st.set_value(i, v)


# Driver code

if __name__ == "__main__":
    main()
