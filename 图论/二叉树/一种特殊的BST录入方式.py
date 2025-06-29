'''
例题: https://codeforces.com/contest/1929/problem/F
BST给出发方式:
5
2 3 -1
-1 -1 2
4 -1 3
-1 5 -1
-1 -1 -1
====
结点总数
左二子  右儿子  val
...
'''

#知识stack: 1,lucas组合  2,二叉树垂序遍历  

#整体答案代码
'''2023年12月17日14:57:16, ac上抄的'''
from string import ascii_lowercase

'''cf的 py3.8 没有cache'''
# from sortedcontainers import *  #cf没有
# from math import *    #pow !
from heapq import *
from collections import *
from bisect import *
from itertools import *
from functools import lru_cache
from copy import *
import sys


# sys.setrecursionlimit(2147483647)  #pypy卡这个...

def main():
    # from math import gcd, floor, ceil, sqrt, isclose, pi, sin, cos, tan, asin, acos, atan, atan2, hypot, degrees, radians, log, log2, log10
    # from heapq import heappush, heappop, heapify, heappushpop, heapreplace, nlargest, nsmallest
    # from itertools import count, cycle, accumulate, chain, groupby, islice, product, permutations, combinations, combinations_with_replacement
    # inf = 3074457345618258602  #注意一下
    mod = 998244353  #ac

    def py():
        print("Yes")  # ac严谨

    def pn():
        print("No")

    # 按照输入的行, 一行一行的取值,每行得到的值都是列表.
    input = lambda: sys.stdin.readline().rstrip()  ##一个是神奇的卡点...
    il = lambda: list(map(int, input().split()))  # 单个 n = i()[0]  列表 l = i() #input_list
    ix = lambda: il()[0]  # 单个数字  #input_x
    # 列表输出数字串, 例子 [1,2,3] printout: 1 2 3
    pl = lambda a: print(" ".join(map(str, a)))  # print_list
    en = enumerate

    def pairwise(a):
        ans = []
        n = len(a)
        for i in range(n - 1):
            ans += (a[i], a[i + 1]),
        return ans

    '''代码'''

    MOD = 998244353
    MX = 5 * 10 ** 5
    ##类似lucas  做一个mod优化的 comb
    class Combinatorics:
        def __init__(self, MX):
            self.f = [1] * (MX + 1)
            self.g = [1] * (MX + 1)
            for i in range(2, MX + 1):
                self.f[i] = self.f[i - 1] * i % MOD
            self.g[-1] = pow(self.f[-1], -1, MOD)
            for i in range(MX, 1, -1):
                self.g[i - 1] = self.g[i] * i % MOD

        def fact(self, n):
            return self.f[n]

        def fact_inv(self, n):
            return self.g[n]

        def comb(self, n, m):
            res = 1
            for x in range(n, n - m, -1):
                res = res * x % MOD
            return (res * self.fact_inv(m)) % MOD

    C = Combinatorics(MX)


    ttt = ix()
    for _ in range(ttt):
        n, lim = il()
        lefts = [-1] * n
        rights = [-1] * n
        vals = [-1] * n
        for i in range(n):
            l, r, v = il()
            if l != -1:
                lefts[i] = l - 1
            if r != -1:
                rights[i] = r - 1
            vals[i] = v
        # print(lefts )
        # print(rights )
        # print(vals )
        seq = [1]
        stk = []
        node = 0
        while stk or node != -1:
            if node != -1:
                stk.append(node)
                node = lefts[node]
            else:
                node = stk.pop()
                seq.append(vals[node])
                node = rights[node]
        seq.append(lim)
        #垂直顺序遍历出来的二叉树, 并且把 1 和 lim加载了头尾
        # print(seq)   #[1, 2, -1, -1, -1, 3, 5]; 形式处理好了,限制需要对每段连续-1单独判断
        ans = 1
        i = 0
        while i < n + 2:
            j = i + 1
            while j < n + 2 and seq[j] == -1:
                j += 1
            if j == n + 2:
                break
            ans = ans * C.comb(seq[j] - seq[i] + j - i - 1, j - i - 1) % MOD
            i = j
        print(ans)





    ''''''


main()

'''test

'''

