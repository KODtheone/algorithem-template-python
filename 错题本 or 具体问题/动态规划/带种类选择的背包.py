'''
https://atcoder.jp/contests/abc383/tasks/abc383_f

问题陈述:
商店中有 N 件商品出售。
第 i 件产品的价格为 Pi日元，效用为 Ui ，颜色为 Ci。您将选择购买这些 N 产品的某个子集(可能没有)。
所选产品的总价不得超过 X 日元。
您的满意度是 S+T×K ，其中 S 是所选产品的效用总和。
T 是所选产品中不同颜色的数量。
这里，K 是给定的常数。

您将选择产品，以最大限度满足您的需求。找到最大限度的满足。

# 在常规背包, 求出最大 s的同时 ,还需要根据 选择 color 的数量 求出种类t * k的贡献
2024年12月7日21:58:28,  结果这个程序还是挺简单的...  关键在于转移方程 ,没想出来.
tag:  带颜色的背包问题
'''

N, X, K = map(int, input().split())
DPs = [[0] * (X + 1) for _ in range(N + 1)]
Items = [[] for _ in range(N)]
for i in range(N):
    p, u, c = map(int, input().split())
    c -= 1
    Items[c].append((p, u))
for i in range(N):
    for j in range(len(Items[i])):
        (p, u) = Items[i][j]
        for k in range(X, -1, -1):
            if(k + p <= X):
                DPs[i + 1][k + p] = max(DPs[i][k] + u + K,DPs[i + 1][k] + u, DPs[i + 1][k + p])
                # 核心, 将同color的物品, 合并到一起, 这样跑到新color的时候 t + 1
                # 转移: 选中, 并且作为新color, 所以 +u+K;  选中, 作为旧color, 所以 +u; 不选,  所以不变
    for k in range(X + 1):
        DPs[i + 1][k] = max(DPs[i + 1][k], DPs[i][k])
print(DPs)
print(max(DPs[N]))