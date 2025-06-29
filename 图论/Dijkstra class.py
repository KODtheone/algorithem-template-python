'''
原自需要返回 具体路径的一道例题:https://leetcode.cn/problems/find-edges-in-shortest-paths/ 见我的题解
class功能  输入, n 节点数  g2, 2形连通图(带wt)
查询 .q_dists(start) 返回start到其他点的最小距离; 是一个列表
查询2 .q_ways(start, end) 返回start到end的所有最短具体路径
#2024年4月22日17:52:03,似乎还应该加上一个, 最短路径共有多少条?    .q_ways的结果len()就行,不过似乎稍微绕路了

##2024年6月22日14:55:52,  q_ways 应用在稠密图上似乎有问题...
'''
from heapq import heappop, heappush
from math import inf


class Djk():
    def __init__(self, n, g2):
        self.n = n
        self.g2 = g2

    def q_dist(self, start):  #询问start为起点,到其他所有点的最小值
        dist = [inf] * self.n
        dist[start] = 0
        pq = [(0, start)]  # idx 0的0是距离而不是点
        while pq:
            curDist, cur = heappop(pq)
            if dist[cur] < curDist:
                continue
            for next, weight in self.g2[cur]:
                cand = dist[cur] + weight
                if cand < dist[next]:
                    dist[next] = cand
                    heappush(pq, (dist[next], next))
        return dist

    def q_ways(self, start, end):
        dist = [inf] * self.n
        dist[start] = 0
        pre = [set()] * self.n  # 增加pre,用于储存最短路径前一个点
        pre[start] = None
        pq = [(0, start)]  # idx 0的0是距离而不是点
        while pq:
            curDist, cur = heappop(pq)
            if dist[cur] < curDist:
                continue
            for next, weight in self.g2[cur]:
                cand = dist[cur] + weight
                if cand < dist[next]:
                    dist[next] = cand
                    pre[next] = set([cur])
                    heappush(pq, (dist[next], next))
                if cand == dist[next]:
                    pre[next].add(cur)
        ways = [[end]]
        res = []  # 存储路径结果(反向的)
        while ways:
            t = ways.pop()
            if (tn := t[-1]) != start:  # (start)
                for x in pre[tn]:
                    ways.append(t + [x])
            else:
                res += [t]
        return [x[::-1] for x in res]

#纯享版  ( heapq 稀疏图)   O(m*logm) m为边数  (如果稠密, m近似n^2,  (n-1)*n//2, 于是 O(n^2 *logn) )
class Djk():
    def __init__(self, g2):
        self.n = len(g2)
        self.g2 = g2

    def q_dist(self, start):
        dist = [inf] * self.n
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            curDist, cur = heappop(pq)
            if dist[cur] < curDist:   continue
            for next, weight in self.g2[cur]:
                cand = dist[cur] + weight
                if cand < dist[next]:
                    dist[next] = cand
                    heappush(pq, (dist[next], next))
        return dist

    def q_ways(self, start, end):
        dist = [inf] * self.n
        dist[start] = 0
        pre = [set()] * self.n
        pre[start] = None
        pq = [(0, start)]
        while pq:
            curDist, cur = heappop(pq)
            if dist[cur] < curDist:   continue
            for next, weight in self.g2[cur]:
                cand = dist[cur] + weight
                if cand < dist[next]:
                    dist[next] = cand
                    pre[next] = set([cur])
                    heappush(pq, (dist[next], next))
                if cand == dist[next]:   pre[next].add(cur)
        ways = [[end]]
        res = []
        while ways:
            t = ways.pop()
            if (tn := t[-1]) != start:
                for x in pre[tn]:    ways.append(t + [x])
            else:   res += [t]
        return [x[::-1] for x in res]


# 纯享版   第二种: 朴素 Dijkstra（适用于稠密图） O(n*n) n为点的数量
# 2024年7月18日11:15:55, 感觉堆优化适用性更高...
class Djk():
    def __init__(self, g2):
        self.n = len(g2)
        self.g2 = g2

    def q_dist(self, start):
        dis = [inf] * self.n
        dis[start] = 0
        done = [False] * self.n
        while True:
            x = -1
            for i, ok in enumerate(done):
                if not ok and (x < 0 or dis[i] < dis[x]):
                    x = i
            if x < 0:
                return dis
            done[x] = True
            for y, w in self.g2[x]:
                dis[y] = min(dis[y], dis[x] + w)