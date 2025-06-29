from test0 import inf

## 2024年4月16日09:00:27, 建图的两种形式:
#1, flody形式  是一位二维列表  g[i][j] = w 代表 i连向j, 路程为w; 若没有路程值,只考虑联通可以用0和1 0表示接通, 1表示不通  运行flody后, 距离大于0,则说明不通;  #感觉麻烦了啊...
#2, 递归形式   g[i] += j,  得出 g[i] = [a,b,c]  说明i点和a,b,c点是联通的   也可以加上w  g[i] = [[a,w1],[b,w2],[c,w3]]
#我自己的建图规定 g1 是矩阵式建图 , g2是联通式建图


roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
#形式   点1 点2  通路权重   同带有weight的 edges
n = 3  #不同的 点 数   也可以从roads中用set扒出来, 但力扣一般都给,所以没必要

##有重复的, 取权重更小的; flody形式 # 1形
g = [[inf] * n for _ in range(n)]
for i in range(n):
    g[i][i] = 0  #自己到自己距离是0,话说会用到吗...
for x, y, wt in roads:
    g[x][y] = min(g[x][y], wt)
    g[y][x] = min(g[y][x], wt)

##无重复; flody形式
g = [[0] * n for _ in range(n)]
for i in range(n):
    g[i][i] = 0  #自己到自己距离是0,话说会用到吗...
for x, y, wt in roads:
    g[x][y] = wt
    g[y][x] = wt

##无权重  进入edge形式;    无环无向  uag, undirected acyclic graph   (有向无环图dag Directed Acyclic Graph)
# n 个点,就会有n-1条边;   #形式2
edges = [[0,1],[1,2],[1,3],[4,2]]   #注意id起点 是0还是1  ; 这个是0的
n = len(edges) + 1
g = [[] for _ in range(n)]
for a,b in edges:
    g[a] += b,
    g[b] += a,
print(g)

#上面edges也可以带weight,  g[a] = [b, w]...
g2 = [[] for _ in range(n)]
for a,b,w in edges:
    g2[a] += (b,w),
    g2[b] += (a,w),  #单向则注掉
print(g2)



# 去重
see = {}
g = [[] for _ in range(n)]
for a, b, w in edges:
    if a == b: continue
    if a > b: a, b = b, a
    if (a, b) in see:
        see[(a, b)] = min(see[(a, b)], w)
    else:
        see[(a, b)] = w
for a, b in see:
    w = see[(a, b)]
    g[a] += [b, w],
    g[b] += [a, w],




#形式1,2 相互转化
#1转2:  已知形式1的图 g1, 无路程值, w=1表示联通, w=0表示不通; n个点 = len(g1)
#参数只有一个: g1
n = len(g1)
g2 = []
for i in range(n):
    tem = []
    for j in range(n):
        if g1[i][j] == 1 and i != j:
            tem += j,
    g2 += [tem]






