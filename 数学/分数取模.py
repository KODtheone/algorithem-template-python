'''
2024年6月30日21:18:35, 遇到: https://atcoder.jp/contests/abc360/tasks/abc360_e    E - Random Swaps of Balls
又需要对分数取模了

所以分数b/a 模 p的结果就为b* a**(p-2) % p
即 b 乘以 a的模p逆元
'''

p = 998244353
a = 3
na = pow(a, p-2, p)
print(na)
b = 1
ans = b * na
## 更方便的计算方法:
na = pow(a, -1, p)  ##  直接写-1 就完事了, 也是说明对  1/a 取模,没毛病!
print(na)


## 另外, 本题的题解:
##  对于1一以外的球 ,  可以视作以 号码为平均值的一个大球,  因为 除了1号以外的球,  是黑球的概率相等.
##  然后就可以开始dp了,  分为 从1到大 和 从大到1两种转移   每次交换对应一次转移

N, K = map(int, input().split())
MOD = 998244353

dp = [[0, 0] for _ in range(K + 1)]
dp[0][0] = 1
for i in range(K):
    p = 2 * (N - 1) * pow(N, -2, MOD) % MOD
    q = 2 * pow(N, -2, MOD)    # pow(N, -2, MOD) 其实就是 N方分之1 , 1/(N*N)
    dp[i + 1][0] = (dp[i][0] * (1 - p) + dp[i][1] * q) % MOD
    dp[i + 1][1] = (dp[i][0] * p + dp[i][1] * (1 - q)) % MOD
print(dp)
print((1 * dp[K][0] + (2 + N) * pow(2, -1, MOD) * dp[K][1]) % MOD)





