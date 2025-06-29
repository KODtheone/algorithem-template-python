'''
2024年8月7日08:23:46,
力扣题目: 3245. 交替组 III   https://leetcode.cn/problems/alternating-groups-iii/description/

树状数组应用:  是求一个集合里大于等于 s 的所有元素之和; 用树状数组即可在 O(logA) 的时间内方便地求出来
我们需要两个树状数组求出答案，一个树状数组维护大于等于 s 的 li 之和，另一个树状数组维护大于等于 s 的 li 有几个。

2024年8月18日10:22:48, 都是可以用线段树代替的,我以后就都用线段树代替树状数组了

'''


class FenwickTree:
    def __init__(self, n):
        self.t = [[0, 0] for i in range(n + 1)]  # 二维的记录 直接把 值也算出来

    def update(self, size, op):
        i = len(self.t) - size
        while i < len(self.t):
            self.t[i][0] += op
            self.t[i][1] += op * size
            i += i & -i

    def query(self, size):
        cnt = s = 0
        i = len(self.t) - size
        while i > 0:
            cnt += self.t[i][0]
            s += self.t[i][1]
            i &= i - 1
        return cnt, s

class Solution:
    def numberOfAlternatingGroups(self, a: List[int], queries: List[List[int]]) -> List[int]:
        n = len(a)
        from sortedcontainers import SortedList
        sl = SortedList()
        t = FenwickTree(n)

        def update(i, op):
            idx = sl.bisect_left(i)
            pre = sl[idx - 1]  # 直接考虑环了, idx = 0 往前会变-1, 往后没有的话, 用 mod
            nxt = sl[idx % len(sl)]
            t.update((nxt - pre - 1) % n + 1, -op)  # 直接配合了ft里面的update
            t.update((i - pre) % n, op)
            t.update((nxt - i) % n, op)

        def add(i):
            if not sl:
                t.update(n, 1)
            else:
                update(i, 1)
            sl.add(i)

        def remove(i):
            sl.remove(i)
            if not sl:
                t.update(n, -1)
            else:
                update(i, -1)

        for i, c in enumerate(a):
            if c == a[(i + 1) % n]: add(i)
        ans = []
        for q in queries:
            if q[0] == 1:
                if not sl:
                    ans += n,
                else:
                    cnt, s = t.query(q[1])
                    ans += s - cnt * (q[1] - 1),
            else:
                i, c = q[1], q[2]
                if a[i] == c:
                    continue
                pre, nxt = (i - 1) % n, (i + 1) % n
                if a[pre] == a[i]:
                    remove(pre)
                if a[i] == a[nxt]:
                    remove(i)
                a[i] = c
                if a[pre] == a[i]: add(pre)
                if a[i] == a[nxt]: add(i)
        return ans
