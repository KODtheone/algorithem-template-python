'''
2024年9月6日11:14:24, 原题: https://leetcode.cn/problems/minimum-number-of-moves-to-seat-everyone/description/
系考题, 凳子的数量m 大于人数n,  每个人只要都能找到凳子就可以

2024年9月6日11:28:29,想不出来怎么做了...
2024年9月6日11:59:29, 似乎写出来了
2024年9月6日12:03:52,再扩展, 思考题, 变成二维空间

2024年10月21日09:56:48   O(i*j)
题意  a: m个凳子的坐标  b: n个人的坐标    返回值:  最少移动次数
'''


class Solution:
    def minMovesToSeat(self, a: List[int], b: List[int]) -> int:
        n, m = len(a), len(b)
        a.sort()
        b.sort()

        @cache
        def dfs(i=0, j=0):
            if i == n: return 0
            # if j == m: return inf
            if m - j < n - i: return inf
            return min(dfs(i, j + 1), dfs(i + 1, j + 1) + abs(a[i] - b[j]))

        ans = dfs()
        dfs.cache_clear()
        return ans