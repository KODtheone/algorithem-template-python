'''
2024年10月25日15:39:09
3317. 安排活动的方案数
https://leetcode.cn/problems/find-the-number-of-possible-ways-for-an-event/description/

组合 求情况数:
把 n 个人划分成 i 个非空集合的方案数（这 i 个集合没有顺序），即第二类斯特林数 S(n,i)。

# 递推第二类斯特林数 也可以看成是dp
'''

MOD = 1_000_000_007
MX = 1001

s = [[0] * MX for _ in range(MX)]
s[0][0] = 1
for i in range(1, MX):
    for j in range(1, i + 1):
        s[i][j] = (s[i - 1][j - 1] + j * s[i - 1][j]) % MOD

class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        ans = 0
        perm = pow_y = 1
        for i in range(1, min(n, x) + 1):
            perm = perm * (x + 1 - i) % MOD
            pow_y = pow_y * y % MOD
            ans += perm * s[n][i] * pow_y
        return ans % MOD