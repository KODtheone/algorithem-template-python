'''
1976. 到达目的地的方案数
https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/solutions/2668041/zai-ji-suan-zui-duan-lu-de-tong-shi-dpfu-g4f3/?envType=daily-question&envId=2024-03-05
一个清楚的视频解释:https://www.bilibili.com/video/BV1zz4y1m7Nq/
#视频有个问题,没有说距离相等怎么处理 比如 如果结点1和7到结点0的距离都是1,那么更新标记哪个?   但是,代码的使用应该是没有问题的.. 我猜猜,应该是更新其中一个最小,然后继续进行. 因为距离都是正的,所以第二次更新标记的一定是第二个同值的最小值
所以, Dijkstra 只适合做 固定两个结点之间的最短路径, 并且,还不能有路径负值存在; 有负数需要使用Bellman-Ford
'''
from heapq import heappop, heappush
from math import inf
from typing import Sequence, Tuple, List

'''
更直接的板子:https://leetcode.cn/problems/network-delay-time/solutions/2668220/liang-chong-dijkstra-xie-fa-fu-ti-dan-py-ooe8/
743. 网络延迟时间
Dijkstra分两种, 稠密图和稀疏图;  n个结点,其中的边越多越稠密  理论上最多n*(n-1)/2条边
'''
#功能: dijkstra求出起点到各点的最短距离 时间复杂度O((V+E)logV); 固定一个起点的
#注意, 可以单向;  堆优化 Dijkstra（适用于稀疏图）
#参数三个: n:图中的节点个数 g: 建好的图,形式为带weight的连通图; start为需要计算的点
def dijkstra1(n: int, g2: Sequence[Sequence[Tuple[int, int]]], start: int) -> List[int]:
    dist = [inf] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        curDist, cur = heappop(pq)
        if dist[cur] < curDist:
            continue
        for next, weight in g2[cur]:
            cand = dist[cur] + weight
            if cand < dist[next]:
                dist[next] = cand
                heappush(pq, (dist[next], next))
    return dist

#测试:
start = 2
# edges = [[(3,5),(1,1),(2,2)],[(3,1)],[],[(0,5),(1,1)],[]]
roads = [[2,1,1],[2,3,1],[3,4,1], [0,4,10]]
n = 5
g2 = [[] for _ in range(n)]
for a,b,w in roads:
    g2[a] += (b,w),
print(dijkstra1(n,g2,start))

#第二种: 朴素 Dijkstra（适用于稠密图）
#注意,这里的图g是 矩阵形式;  1形
def dijkstra2(n: int, g1: Sequence[Sequence[Tuple[int, int]]], start: int) -> List[int]:
        dis = [inf] * n
        ans = dis[start] = 0
        done = [False] * n
        while True:
            x = -1
            for i, ok in enumerate(done):
                if not ok and (x < 0 or dis[i] < dis[x]):
                    x = i
            if x < 0:
                return dis
            done[x] = True  # 最短路长度已确定（无法变得更小）
            for y, d in enumerate(g1[x]):
                dis[y] = min(dis[y], dis[x] + d)

g1 = [[inf for _ in range(n)] for _ in range(n)]  # 邻接矩阵
roads = [[2,1,1],[2,3,1],[3,4,1], [0,4,10]]
for x, y, d in roads:
    g1[x ][y ] = d
print(dijkstra2(n, g1, start))
