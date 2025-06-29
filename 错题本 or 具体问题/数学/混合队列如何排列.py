'''
2024年12月9日09:22:07

作为步骤中的一个基本问题   例如,  第一种操作有3步(顺序固定),  第二种操作有5步,  那么将这两种操作组合成一个操作,  有8步, 总共有多少种组合方式?
#  额, 貌似用组合就完事了...
例题: https://atcoder.jp/contests/arc189/tasks/arc189_a
题解: https://atcoder.jp/contests/arc189/editorial/11558

'''

import sys
import itertools

def factorial(N, MOD):
    fact = 1
    for i in range(2, N+1):
        fact *= i
        fact %= MOD
    return fact

def solve(N, A):
    MOD = 998244353
    cnts = [len(list(v)) for _, v in itertools.groupby(A)]
    # print(cnts)
    if A[0] == 0 or any(cnt%2 == 0 for cnt in cnts):
        return 0

    nums = [1, 1]
    for i in range(5, max(cnts)+1, 2):
        nums.append((i-2) * nums[-1] % MOD)

    res = factorial(sum(cnt//2 for cnt in cnts), MOD)
    for cnt in cnts:
        if cnt == 1:
            continue
        res *= nums[cnt//2]
        res *= pow(factorial(cnt//2, MOD), -1, MOD)  # 阶乘的逆元,  其实是除法
        res %= MOD
    return res  % MOD

def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    res = solve(N, A)
    print(res)

if __name__ == "__main__":
    main()
'''
8
1 1 1 1 1 1 1 0
# n 不重要 
799   
1 1 1 1 1 1 1 
#3 + 2 也就是  7 + 5
1 
1 1 1 1 1 1 1 0 1 1 1 1 1 
# 3 + 2 + 2
1 
1 1 1 1 1 1 1 0 1 1 1 1 1 0 1 1 1 1 1    

#  验证 , 正确! 
操作时  直接统计连续相同字段的个数  不然就重新计算.    x长的折算成  x // 2  ( 不能有偶数 , 不然是不合法的 )


'''

