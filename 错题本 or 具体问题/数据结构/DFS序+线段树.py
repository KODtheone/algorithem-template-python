'''
2024年8月9日19:50:19 https://leetcode.cn/problems/coin-bonus/description/
LCP 05. 发 LeetCoin
神奇的 DFS序+线段树

2024年8月9日19:50:51, 看的不是很懂,  dfs建立出来的L,R 好像只有这么一下小改动

ps: 此题有一个 树状数组 区间更新的 题解: https://leetcode.cn/problems/coin-bonus/solutions/945513/xiao-ai-lao-shi-li-kou-bei-li-jie-zhen-t-rut3/


'''


class Solution:

    def __init__(self):
        self.LEN = 50005
        self.G = [[] for _ in range(self.LEN)]
        self.cnt = 1
        self.L, self.R = [0 for _ in range(self.LEN)], [0 for _ in range(self.LEN)]
        self.sum = [0 for _ in range(self.LEN * 4)]
        self.add = [0 for _ in range(self.LEN * 4)]
        self.MOD = 10 ** 9 + 7

    def dfs(self, u):
        self.cnt += 1
        self.L[u] = self.cnt
        for v in self.G[u]:
            self.dfs(v)
        self.R[u] = self.cnt

    def mod(self, num):
        return num % self.MOD

    def push_up(self, rt: int):
        self.sum[rt] = self.sum[rt * 2] + self.sum[rt * 2 + 1]
        self.sum[rt] = self.mod(self.sum[rt])

    def push_down(self, rt: int, m: int):
        if (self.add[rt] != 0):
            self.add[rt << 1] += self.add[rt]
            self.add[rt << 1] = self.mod(self.add[rt << 1])

            self.add[rt << 1 | 1] += self.add[rt]
            self.add[rt << 1 | 1] = self.mod(self.add[rt << 1 | 1])

            self.sum[rt << 1] += self.add[rt] * (m - (m >> 1))
            self.sum[rt << 1] = self.mod(self.sum[rt << 1])

            self.sum[rt << 1 | 1] += self.add[rt] * (m >> 1)
            self.sum[rt << 1 | 1] = self.mod(self.sum[rt << 1 | 1])
            self.add[rt] = 0

    def update_single(self, p: int, val: int, l: int, r: int, rt):
        if l == r:
            self.sum[rt] += val
            self.sum[rt] = self.mod(self.sum[rt])
            return
        self.push_down(rt, r - l + 1)
        m = (l + r) >> 1
        if p <= m:
            self.update_single(p, val, l, m, rt << 1)
        else:
            self.update_single(p, val, m + 1, r, rt << 1 | 1)
        self.push_up(rt)

    def update_range(self, L: int, R: int, c: int, l: int, r: int, rt: int):
        if L <= l <= r <= R:
            self.add[rt] += c
            self.add[rt] = self.mod(self.add[rt])
            self.sum[rt] += c * (r - l + 1)
            self.sum[rt] = self.mod(self.sum[rt])
            return
        self.push_down(rt, r - l + 1)
        m = (l + r) // 2
        if L <= m:
            self.update_range(L, R, c, l, m, rt << 1)
        if m < R:
            self.update_range(L, R, c, m + 1, r, rt << 1 | 1)
        self.push_up(rt)

    def query(self, L: int, R: int, l: int, r: int, rt: int):
        if L <= l <= r <= R:
            return self.sum[rt]
        self.push_down(rt, r - l + 1)
        m, ret = (l + r) // 2, 0
        if L <= m:
            ret += self.query(L, R, l, m, rt << 1)
            ret = self.mod(ret)
        if m < R:
            ret += self.query(L, R, m + 1, r, rt << 1 | 1)
            ret = self.mod(ret)
        return ret

    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        for l in leadership:
            self.G[l[0]].append(l[1])
        self.dfs(1)
        ans = []
        for op in operations:
            if op[0] == 1:
                self.update_single(self.L[op[1]], op[2], 1, self.cnt, 1)
            elif op[0] == 2:
                self.update_range(self.L[op[1]], self.R[op[1]], op[2], 1, self.cnt, 1)
            elif op[0] == 3:
                ans.append(self.query(self.L[op[1]], self.R[op[1]], 1, self.cnt, 1) % self.MOD)
                # print(ans)
        return ans