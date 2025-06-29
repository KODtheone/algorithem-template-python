'''
例题:https://codeforces.com/contest/1931/problem/G

2024年6月10日15:31:38, 另外我发现一个性质,a,b特别的大的时候 算出来一定是0, 猜测是超过mod之类的原因,擦侧因为 x ** mod % mod = x 之类的原因....
'''
from functools import cache
from random import randint


# 纯享版:
def get_comb(a, b, p):
    if b > a:      return 0
    if b > a - b:  b = a - b
    u = d = 1
    for i in range(b):
        u = (u * (a - i)) % p
        d = (d * (b - i)) % p
    return (u * pow(d, p - 2,p)) % p
def comb(a, b, p):
    if b == 0:   return 1
    return (comb(a // p, b // p,p) * get_comb(a % p, b % p,p)) % p


#使用:  lucas(a,b,p) 相当于求 comb(a,b) % p  跟pow差不多的原理,大大提高计算速度
# @cache   # 加cache 可能有用,也可能有不良影响...;  总之意义不大,还平白增加了空间复杂度,也是拖慢时间的...
def fast_pow(a, b, p):  # p 就是 mod
    ans = 1
    while b:
        if b & 1:
            ans = (ans * a) % p
        a = (a ** 2) % p
        b >>= 1
    return ans
# @cache
def getCombination(a, b, p):
    if b > a:
        return 0
    if b > a - b:
        b = a - b
    u = 1
    d = 1
    for i in range(b):
        u = (u * (a - i)) % p
        d = (d * (b - i)) % p
    return (u * fast_pow(d, p - 2,p)) % p
# @cache
def lucas(a, b, p):
    if b == 0:
        return 1
    return (lucas(a // p, b // p,p) * getCombination(a % p, b % p,p)) % p

mod = 998244353
print(lucas(1800000, 900000, mod)*lucas(1800000, 900000, mod)%mod)


###时间验证

def get_comb(a, b, p):
    if b > a:      return 0
    if b > a - b:  b = a - b
    u = d = 1
    for i in range(b):
        u = (u * (a - i)) % p
        d = (d * (b - i)) % p
    return (u * pow(d, p - 2,p)) % p

def comb(a, b, p):
    if b == 0:   return 1
    return (comb(a // p, b // p,p) * get_comb(a % p, b % p,p)) % p

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        return comb(n-1+k,k,10**9 + 7)

for i in range(100):
    a= randint(1,1000000)
    b= randint(1,a)
    print(a,b)
    print(Solution().valueAfterKSeconds(a, b))



#  2024年12月29日15:41:11  相同作用:  杨潇的 Factorial模版
class Factorial:
    def __init__(self, N, mod) -> None:
        N += 1
        self.mod = mod
        self.f = [1 for _ in range(N)]
        self.g = [1 for _ in range(N)]
        for i in range(1, N):
            self.f[i] = self.f[i - 1] * i % self.mod
        self.g[-1] = pow(self.f[-1], mod - 2, mod)
        for i in range(N - 2, -1, -1):
            self.g[i] = self.g[i + 1] * (i + 1) % self.mod

    def fac(self, n):
        return self.f[n]

    def fac_inv(self, n):
        return self.g[n]

    def combi(self, n, m):
        if n < m or m < 0 or n < 0: return 0
        return self.f[n] * self.g[m] % self.mod * self.g[n - m] % self.mod

    def permu(self, n, m):
        if n < m or m < 0 or n < 0: return 0
        return self.f[n] * self.g[n - m] % self.mod

    def catalan(self, n):
        return (self.combi(2 * n, n) - self.combi(2 * n, n - 1)) % self.mod

    def inv(self, n):
        return self.f[n-1] * self.g[n] % self.mod

fac = Factorial(10 ** 5, mod)

## 2025年5月11日09:16:59，  这个 class 更好， 因为直接包括了预处理！
# 例子 https://atcoder.jp/contests/abc405/tasks/abc405_e   这道题， 不用预处理依然会超时 见我的提交
