'''
1928. 规定时间内到达终点的最小花费
https://leetcode.cn/problems/minimum-cost-to-reach-destination-in-time/
https://leetcode.cn/problems/minimum-cost-to-reach-destination-in-time/solutions/2937601/chao-yue-98de-dijkstrayou-hua-si-lu-by-c-fipw/?envType=daily-question&envId=2024-10-03

dp可以做,但是时间很慢
2024年10月3日11:48:53, 优化的解法 ,用的好像确实是 类似 Dijkstra的思路  堆优化 ,
超时的不会进堆, 能进堆的按最小费顺序出
nt >= f[x]: # f 在外部记录, 到达x点的最短时间   是为了更好的去重
第一维的排序是 fee, 第二维排序, 最短时间用于排除重复路线, (不然这一个有环图, 后面点会无限重复进堆)
如果fee更大, 而时间也更大,那当然应该.    或者,fee更大,但是时间更小了, 有可能前面fee更小的那次通过, 走到后面超时了, 所以后面fee更大,但时间小的这次才需要保留.
# 第一位队列 fee 按顺序出.   类似0,1,2,3 到 inf 的出fee 但是这样fee大了做不了 , 而这样有进才有出, 属于 离散化
有点二维排序的意思  两成排序给考虑清楚了...
'''


class Solution:
    def minCost(self, mt: int, edges: List[List[int]], pf: List[int]) -> int:
        n = len(pf)
        g = [[] for i in range(n)]
        for x, y, t in edges:
            g[x] += (y,t),
            g[y] += (x,t),
        f = [inf] * n
        f[0] = 0
        st = [(pf[0], 0, 0)]
        while st:
            cost, pos, time = heappop(st)
            if pos == n - 1:
                return cost
            for x, t in g[pos]:
                print(f)
                nt = time + t
                if nt > mt or nt >= f[x]: # f 在外部记录, 到达x点的最短时间
                # if nt > mt:
                    continue
                f[x] = nt
                heappush(st, (cost + pf[x], x, nt))
        return -1