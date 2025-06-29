'''
2024年6月30日15:52:55, 来自力扣: 100318. 合并两棵树后的最小直径   和   310. 最小高度树
https://leetcode.cn/problems/find-minimum-diameter-after-merging-two-trees/description/        https://leetcode.cn/problems/minimum-height-trees/description/
一棵树的 直径 指的是树中任意两个节点之间的最长路径长度。


'''
from collections import deque


#  功能:  计算树的直径  一个int
#  参数:  edges 形式给出的数   则其节点数 n = len(edges) + 1
def f(edges):
    n = len(edges) + 1
    if n == 1:  return 0   # 这里必须特判
    g = [[] for _ in range(n)]
    degree = [0] * n
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)
        degree[a] += 1
        degree[b] += 1
    q = deque(i for i in range(n) if degree[i] == 1)
    dia = 0
    while 1:
        dia += 2
        for _ in range(len(q)):
            a = q.popleft()
            for b in g[a]:
                degree[b] -= 1
                if degree[b] == 1:
                    q.append(b)
        if len(q) == 1: break
        elif len(q) == 0: dia -= 1;break
    return dia

# 纯享版
def f(edges):
    n = len(edges) + 1
    if n == 1:  return 0
    g = [[] for _ in range(n)];degree = [0] * n
    for a, b in edges: g[a].append(b);g[b].append(a); degree[a] += 1;degree[b] += 1
    q = deque(i for i in range(n) if degree[i] == 1);dia = 0
    while 1:
        dia += 2
        for _ in range(len(q)):
            a = q.popleft()
            for b in g[a]:
                degree[b] -= 1
                if degree[b] == 1:  q.append(b)
        if len(q) == 1: break
        elif len(q) == 0: dia -= 1;break
    return dia

edges1 = [[0,1],[0,2],[0,3]]
print(f(edges1))



# 纯享版  ( 方法2, 上面的bfs 剥洋葱法)
def f(edges) -> int:
    g = [[] for _ in range(len(edges) + 1)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)
    res = 0
    def dfs(x: int, fa: int):
        nonlocal res
        max_len = 0
        for y in g[x]:
            if y != fa:
                sub_len = dfs(y, x) + 1
                res = max(res, max_len + sub_len)
                max_len = max(max_len, sub_len)
        return max_len
    dfs(0, -1)
    return res


