#1 好写但重复使用时复杂度高,(也可以打表, 也可以@cache,避免重复计算)
from math import isqrt

def is_prime(n: int) -> bool:
    if n <= 1: return False
    return all(n % i for i in range(2, isqrt(n) + 1))

print(is_prime(0),is_prime(1),is_prime(823))

###第二种, 筛选标记法:
# 标记 10**5 以内的质数
2
# print(is_prime)
for i in range(100):
    print(i,is_prime[i])


# 显示所有质数 记录在pr中
MX = 10 ** 6 + 1
is_prime = [True] * MX
is_prime[1] = False
is_prime[0] = False
for i in range(2, MX):
    if is_prime[i]:
        for j in range(i * i, MX, i):
            is_prime[j] = False
pr = []
for i in range(10**6):
    if is_prime[i]:
        pr += i,
# print(pr, len(pr))


''''''
print()