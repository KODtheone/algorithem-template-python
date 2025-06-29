'''
2024年8月10日15:40:18,https://ac.nowcoder.com/acm/contest/87303/E

这道题其实挺简单的,都不知道我当时为什么做错了...
我写的dfs 差了一个等号, 然后, 又被python的dfs  RecursionError: maximum recursion depth exceeded in comparison 给坑了...
# 所以, 还是要多练习使用递推形式
'''

times = 0  # 0有t, 1无t
if not times:
    times = ix()
for _ in range(times):
    n = ix()
    a = il()
    dp = [0] + [inf] * n
    for i, x in enumerate(a):
        for j in range(n + 1 - x)[::-1]:
            if j <= i and j + x >= i :
                dp[j + x] = min(dp[j + x], dp[j] + 1)
    print(dp[n] if dp[n] != inf else -1)