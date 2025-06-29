'''
例题: https://leetcode.cn/problems/find-the-safest-path-in-a-grid/solutions/2375565/jie-jin-on2-de-zuo-fa-duo-yuan-bfsdao-xu-r5um/



'''

# 目的, 给出矩阵grid, 其中有一一些点=1, 代表源, 剩下的点=0
##现在想要求 每个点距离源点的最近距离  (思考题:如果是最远距离怎么办,只能枚举源点了吗?)
#参数:  grid, 原始矩阵
# 返回值,  tuple 2, 1为 距离矩阵dis, 2为所有距离源点i的点 group[i], 最多到i = m+n - 2 对角情况
def multi_source_bfs(grid):
    m, n = len(grid), len(grid[0])
    q = []
    dis = [[-1] * n for _ in range(m)]
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            if x:   #x == 1 , is source
                q.append((i, j))
                dis[i][j] = 0
    groups = [q]   # 多记录了一个 所有长度的group: group[i]中的列表里是所有距离源 i 的点
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 四方向行走,上下左右
    while q:  # 多源 BFS
        tmp = q
        q = []
        for i, j in tmp:
            for di, dj in d :
                if 0 <= (ni:=i+di) < m and 0 <= (nj:=j+dj) < n and dis[ni][nj] < 0:
                    q.append((ni,nj))
                    dis[ni][nj] = len(groups)
        groups.append(q)  # 相同 dis 分组记录
    return dis, groups

#纯享版
def multi_source_bfs(grid):
    m, n = len(grid), len(grid[0])
    q = []
    dis = [[-1] * n for _ in range(m)]
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            if x:
                q.append((i, j))
                dis[i][j] = 0
    groups = [q]
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while q:
        tmp = q
        q = []
        for i, j in tmp:
            for di, dj in d :
                if 0 <= (ni:=i+di) < m and 0 <= (nj:=j+dj) < n and dis[ni][nj] < 0:
                    q.append((ni,nj))
                    dis[ni][nj] = len(groups)
        groups.append(q)
    return dis, groups

# test
g = [[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
a, b = multi_source_bfs(g)
print(a)
print(b, len(b))