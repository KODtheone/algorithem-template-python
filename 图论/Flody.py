'''
原题:https://leetcode.cn/problems/number-of-possible-sets-of-closing-branches/solutions/2560722/er-jin-zhi-mei-ju-floydgao-xiao-xie-fa-f-t7ou/
返回一个g1形, 把所有点之间的距离更新成了最短路距离
2024年6月23日10:25:05, 与djk的区别, 一口气更新所有最短路

'''
from copy import deepcopy
from math import inf
from typing import List

# 方法挺暴力的    二进制枚举, 图 ,Floyd的结合   没什么难度,就是暴力实现
##可以先观察范围 1 <= n <= 10  这个个体数给的这么少,就是让人去暴力了

roads = [[0, 1, 20], [0, 1, 10], [1, 2, 2], [0, 2, 2]]
# 形式   点1 点2  通路权重
n = 3  # 不同的 点 数   也可以从roads中用set扒出来, 但力扣一般都给,所以没必要
g = [[inf] * n for _ in range(n)]
for i in range(n):
    g[i][i] = 0
for x, y, wt in roads:      #g1形, 有重复取最小wt
    g[x][y] = min(g[x][y], wt)
    g[y][x] = min(g[y][x], wt)

f = deepcopy(g)
print(f)

# Floyd
for k in range(n):
    for i in range(n):
        if f[k][i] == inf :continue  #加上应该能快一丢丢,在力扣上卡过速度
        if k == i: continue
        for j in range(n):
            f[i][j] = min(f[i][j], f[i][k] + f[k][j])
print(f)  #[[0, 4, 2], [4, 0, 2], [2, 2, 0]]  正确的,可以只看正三角,反正是返回了对的两点间距离, 另外, 我记得Floyd 其实对单向也成立的
print(g)
