'''
2024年5月11日09:33:40,  课程表系列;
拓扑排序(Topological Sorting)通常用来解决依赖关系问题。
  DAG图（有向无环图 Directed Acyclic Graph）
#重点: 入度  indegree

'''
#基础版,例题, 207.课程表  https://leetcode.cn/problems/course-schedule/description/
# 问题:  给出节点数n, 和结点关系 edges (有向图);  判断是不是生成了无环图
# 参数:  n: 图中点数  edges: 有向关系, 编号从0开始, [0]是[1]的必要条件(例如课程表,需要上完[0],才能上[1])
def ts(n, edges):
    #1,建图, 需要有 indegree
    g = [[] for _ in range(n)]
    deg = [0] * n
    for f, s in edges:
        g[f] += s,
        deg[s] += 1
    #2, 队列,里面放indegree == 0 的, 可想成表示已经解锁
    que = []
    for i in range(n):
        if not deg[i]: que += i,
    #3, bfs
    while que:
        pre = que.pop()
        n -= 1
        for x in g[pre]:
            deg[x] -= 1
            if not deg[x]:
                que += x,
    return not n

#纯享版
def ts(n, edges):
    g = [[] for _ in range(n)]
    deg = [0] * n
    for f, s in edges:
        g[f] += s,
        deg[s] += 1
    que = []
    for i in range(n):
        if not deg[i]: que += i,
    while que:
        pre = que.pop()
        n -= 1
        for x in g[pre]:
            deg[x] -= 1
            if not deg[x]:
                que += x,
    return not n

#另, 210.课程表II : 可返回解锁顺序路径, 可应用于 https://leetcode.cn/problems/build-a-matrix-with-conditions/
# 1462. 课程表 IV : 可以单独查询两个点之间的锁定关系

# 210.课程表II  返回解锁路径:
def findOrder( n: int, edges: List[List[int]]) -> List[int]:
    ans = []
    g = [[] for _ in range(n)]
    deg = [0] * n
    for s, f in edges:
        g[f] += s,
        deg[s] += 1
    que = [i for i in range(n) if not deg[i]]
    while que:
        pre = que.pop()
        ans += pre,
        n -= 1
        for x in g[pre]:
            deg[x] -= 1
            if not deg[x]:
                que += x,
    return [] if n else ans


