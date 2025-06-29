'''
2024年6月26日20:05:09, 有些不太靠
需要注意基底, n的大小  之前取400, 大于400的因子就不收录了...
另外,速度也不快
'''

class Prime:
    def __init__(self, n = 1000000) -> None:
        self.primes = self.prime_list(n)

    def prime_sieve(self, n):
        """returns a sieve of primes >= 5 and < n"""
        flag = n % 6 == 2
        sieve = bytearray((n // 3 + flag >> 3) + 1)
        for i in range(1, int(n ** 0.5) // 3 + 1):
            if not (sieve[i >> 3] >> (i & 7)) & 1:
                k = (3 * i + 1) | 1
                for j in range(k * k // 3, n // 3 + flag, 2 * k):
                    sieve[j >> 3] |= 1 << (j & 7)
                for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                    sieve[j >> 3] |= 1 << (j & 7)
        return sieve

    def prime_list(self, n):
        """returns a list of primes <= n"""
        res = []
        if n > 1:
            res.append(2)
        if n > 2:
            res.append(3)
        if n > 4:
            sieve = self.prime_sieve(n + 1)
            res.extend(
                3 * i + 1 | 1 for i in range(1, (n + 1) // 3 + (n % 6 == 1)) if not (sieve[i >> 3] >> (i & 7)) & 1)
        return res

    def dissolve(self, num):
        '''prime factor decomposition of num'''
        lst = []
        idx = -1
        for prime in self.primes:
            if prime * prime > num:
                break

            if num % prime == 0:
                lst.append([prime, 0])
                idx += 1

            while num % prime == 0:
                lst[idx][1] += 1
                num //= prime

        if num != 1:
            lst.append([num, 1])

        return lst

    def GetAllFactors(self, num, SORT=False):
        res = [1]
        if num == 1:
            return res
        else:
            for a, b in self.dissolve(num):
                mul = a
                k = len(res)
                for _ in range(b):
                    for i in range(k):
                        res.append(res[i] * mul)
                    mul *= a

            if SORT:
                res.sort()

            return res

    def primitive_root(self, num):
        '''
        check whether num is prime
        '''
        g = 1
        DIS = self.dissolve(num)
        while True:
            for a, b in DIS:
                if pow(g, (num - 1) // a, num) == 1:
                    break
            else:
                break
            g += 1
        return g

# test
p = Prime()
# print(p.primes)
# print(p.prime_list(78))  # 输出小于x的所有质数列表
# print(p.prime_list(1134))
# print(p.dissolve(78))       #分解成 [[2, 1], [3, 1], [13, 1]] 形式, 表示, 含1个2,1个3,1个13  总= 2*3*13=78
print(p.dissolve(538084))
538084
# print(p.primitive_root(78))
# print(p.primitive_root(6))  #有问题..
# print(p.GetAllFactors(78578142444))  #[1, 2, 3, 6, 13, 26, 39, 78] 所有因子从小到大排列
# print(p.GetAllFactors(1134))
# # print(p.)
# print(p.dissolve(641239463))
# print(p.dissolve(337739933* 394966669))


'''
2024年7月28日15:22:55,  
第二种  羊的   PrimeTable
'''
class PrimeTable:
    def __init__(self, n: int) -> None:
        self.n = n
        self.primes = []
        self.max_div = list(range(n + 1))
        self.max_div[1] = 1
        self.phi = list(range(n + 1))
        for i in range(2, n + 1):
            if self.max_div[i] == i:
                self.primes.append(i)
                for j in range(i, n + 1, i):
                    self.max_div[j] = i
                    self.phi[j] = self.phi[j] // i * (i - 1)

    def is_prime(self, x: int):
        if x < 2: return False
        if x <= self.n: return self.max_div[x] == x
        for p in self.primes:
            if p * p > x: break
            if x % p == 0: return False
        return True

    def prime_factorization(self, x: int):
        if x > self.n:
            for p in self.primes:
                if p * p > x: break
                if x <= self.n: break
                if x % p == 0:
                    cnt = 0
                    while x % p == 0: cnt += 1; x //= p
                    yield p, cnt
        while (1 < x and x <= self.n):
            p, cnt = self.max_div[x], 0
            while x % p == 0: cnt += 1; x //= p
            yield p, cnt
        if x >= self.n and x > 1:
            yield x, 1

    def get_factors(self, x: int):
        factors = [1]
        for p, b in self.prime_factorization(x):
            n = len(factors)
            for j in range(1, b + 1):
                for d in factors[:n]:
                    factors.append(d * (p ** j))
        return factors

p = PrimeTable(10 ** 5)

'''2024年8月28日14:15:01, 功能说明:
1 初始化, PrimeTable(10 ** 5)  这个数字不能太大,大概是 nlogn的 所以 10**9 不行
2 prime_factorization(self, x: int)  返回所有质数因子和其指数   形式 [(2, 1), (3, 1)...]
    这个x数字可以非常大, 最大质数因子不要超过第一步中获得最大质数即可... ( 不然会拆不开...)
3 get_factors(self, x: int)  返回所有因子, 从小到大排列
    这个的条件限制跟2一样,只不过返回的是所有情况; 用2的结果直接生成的(都没有排序)
'''


# 2024年7月28日15:41:13, 太大会出错, 例如10 ** 9  mle, memory error
p = PrimeTable(10 ** 5).primes
pp = PrimeTable(10 ** 5)
print(p)
print(pp.prime_factorization(878))
print(list(pp.prime_factorization(878)))
print(pp.get_factors(878))
print(pp.get_factors(25))


'''
2024年8月28日14:38:37, 例题应用: https://www.lanqiao.cn/problems/19779/learning/?contest_id=200  6.智算士气
使用质数表,求出所有质数因子和次数.   因为关系是相互独立的,所以直接相乘就可以...
核心代码:
    times = 1  # 0有t, 1无t
    if not times:
        times = ix()
    for _ in range(times):
        n,m = il()
        pp = PrimeTable(10 ** 5 + 100)
        ps = list(pp.prime_factorization(m))
        ans = 1
        for v, c in ps:
            ans *= pow(c + 1, n, mod) - pow(c,n,mod)
            ans %= mod
        print(ans)
'''


