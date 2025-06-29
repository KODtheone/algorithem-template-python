'''
例题:  3276. 选择矩阵中单元格的最大得分   https://leetcode.cn/problems/select-cells-in-grid-with-maximum-score/description/
题解: https://leetcode.cn/problems/select-cells-in-grid-with-maximum-score/solutions/2899994/zhi-yu-zhuang-ya-dppythonjavacgo-by-endl-x27y/
据说是    值域状压dp

这个题解倒是挺清晰的.
2024年9月1日16:33:47, 我觉得应该有别的做法.
我抽象出来的题意:   给出n行的矩阵,从每行最多取出一个值,  所有的取出值不能有重复, 求取出的值的和的最大值.
我感觉是一个反向的并查集问题 ,但是并没有合适的手段来解决它...

2024年9月9日11:18:48,确实可以, 反向并查集的方法,  但是非常复杂...
mcf graph  min cost flow graph 最小流图
匈牙利算法,  是网络流的一个分支;  网络流的用法更普遍.    km算法是匈牙利算法的一个优化
匈牙利算法只能应用于二分图,  判断二分图的方法   染色法dfs,  所有结点能分成两个集合, 集合1内部的点没有边, 只与集合b之间的点有边\

2024年9月9日14:10:52, 果然啊, 小羊这个  mcfg也是从 ac library- python抄的...
https://github.com/not522/ac-library-python/blob/master/atcoder/mincostflow.py
模版说明文件: https://atcoder.github.io/ac-library/production/document_en/mincostflow.html

'''
from heapq import *
from typing import *


# mcf的板子
class MCFGraph:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int
        cost: int

    class _Edge:
        def __init__(self, dst: int, cap: int, cost: int) -> None:
            self.dst = dst
            self.cap = cap
            self.cost = cost
            self.rev: Optional[MCFGraph._Edge] = None

    def __init__(self, n: int) -> None:
        self._n = n
        self._g: List[List[MCFGraph._Edge]] = [[] for _ in range(n)]
        self._edges: List[MCFGraph._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int, cost: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = MCFGraph._Edge(dst, cap, cost)
        re = MCFGraph._Edge(src, 0, -cost)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> Edge:
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = cast(MCFGraph._Edge, e.rev)
        return MCFGraph.Edge(
            re.dst,
            e.dst,
            e.cap + re.cap,
            re.cap,
            e.cost
        )

    def edges(self) -> List[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def flow(self, s: int, t: int,
             flow_limit: Optional[int] = None) -> Tuple[int, int]:
        return self.slope(s, t, flow_limit)[-1]

    def slope(self, s: int, t: int,
              flow_limit: Optional[int] = None) -> List[Tuple[int, int]]:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = cast(int, sum(e.cap for e in self._g[s]))

        dual = [0] * self._n
        prev: List[Optional[Tuple[int, MCFGraph._Edge]]] = [None] * self._n

        def refine_dual() -> bool:
            pq = [(0, s)]
            visited = [False] * self._n
            dist: List[Optional[int]] = [None] * self._n
            dist[s] = 0
            while pq:
                dist_v, v = heappop(pq)
                if visited[v]:
                    continue
                visited[v] = True
                if v == t:
                    break
                dual_v = dual[v]
                for e in self._g[v]:
                    w = e.dst
                    if visited[w] or e.cap == 0:
                        continue
                    reduced_cost = e.cost - dual[w] + dual_v
                    new_dist = dist_v + reduced_cost
                    dist_w = dist[w]
                    if dist_w is None or new_dist < dist_w:
                        dist[w] = new_dist
                        prev[w] = v, e
                        heappush(pq, (new_dist, w))
            else:
                return False
            dist_t = dist[t]
            for v in range(self._n):
                if visited[v]:
                    dual[v] -= cast(int, dist_t) - cast(int, dist[v])
            return True

        flow = 0
        cost = 0
        prev_cost_per_flow: Optional[int] = None
        result = [(flow, cost)]
        while flow < flow_limit:
            if not refine_dual():
                break
            f = flow_limit - flow
            v = t
            while prev[v] is not None:
                u, e = cast(Tuple[int, MCFGraph._Edge], prev[v])
                f = min(f, e.cap)
                v = u
            v = t
            while prev[v] is not None:
                u, e = cast(Tuple[int, MCFGraph._Edge], prev[v])
                e.cap -= f
                assert e.rev is not None
                e.rev.cap += f
                v = u
            c = -dual[s]
            flow += f
            cost += f * c
            if c == prev_cost_per_flow:
                result.pop()
            result.append((flow, cost))
            prev_cost_per_flow = c
        return result