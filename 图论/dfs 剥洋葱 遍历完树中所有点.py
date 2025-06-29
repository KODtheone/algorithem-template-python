''''
2024年7月1日23:04:29

和 计算一颗数的直径有些类似, 不过这里是dfs
同样从 叶子出发 但是不要求bfs的顺序

应用于题目: https://codeforces.com/problemset/problem/1833/G 1800
我的提交: https://codeforces.com/contest/1833/submission/268334822
'''
edges = [[0,1],[2,0],[3,0],[4,0],[5,1]]
# 参数 就是给定的这个edges
# 功能, 遍历了一遍结点, 相当于不断拆下 叶子结点
n = len(edges) + 1
g = [frozenset()] * n
for a,b  in edges:
    g[a] |= {b}
    g[b] |= {a}  # 这样degree就不用单写了,直接 len 一下就是degree
run = [i for i in range(n) if len(g[i]) == 1]
ans = []
while run:
    t = run.pop()
    print(t)
    for nxt in g[t]:
        g[nxt] -= {t}  # 去掉叶子
        if len(g[nxt]) == 1:
            run += nxt,
