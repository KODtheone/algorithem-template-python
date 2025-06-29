'''
2024年8月10日16:54:53  https://atcoder.jp/contests/arc181/tasks/arc181_b B - Annoying String Problem
这题确实超级烦人...

我似乎读题就读错了, t可以完全 等于s 的...
ps: 抄的答案里还有个 rolling hash,  似乎也有用, 跟 kmp什么一类的
其实不需要

'''
import random


class RollingHash:
    mask30 = (1 << 30) - 1
    mask31 = (1 << 31) - 1
    MOD = (1 << 61) - 1
    Base = None
    pw = [1]

    def __init__(self, S):
        if RollingHash.Base is None:
            RollingHash.Base = random.randrange(129, 1 << 30)
        for i in range(len(RollingHash.pw), len(S) + 1):
            RollingHash.pw.append(
                RollingHash.CalcMod(RollingHash.Mul(RollingHash.pw[i - 1], self.__class__.Base))
            )

        self.hash = [0] * (len(S) + 1)
        for i, s in enumerate(S, 1):
            self.hash[i] = RollingHash.CalcMod(
                RollingHash.Mul(self.hash[i - 1], RollingHash.Base) + ord(s)
            )

    def get(self, l, r):
        return RollingHash.CalcMod(
            self.hash[r] - RollingHash.Mul(self.hash[l], RollingHash.pw[r - l])
        )

    def Mul(l, r):
        lu = l >> 31
        ld = l & RollingHash.mask31
        ru = r >> 31
        rd = r & RollingHash.mask31
        middlebit = ld * ru + lu * rd
        return (
            ((lu * ru) << 1)
            + ld * rd
            + ((middlebit & RollingHash.mask30) << 31)
            + (middlebit >> 30)
        )

    def CalcMod(val):
        if val < 0:
            val %= RollingHash.MOD
        val = (val & RollingHash.MOD) + (val >> 61)
        if val > RollingHash.MOD:
            val -= RollingHash.MOD
        return val

from math import gcd


def solve(S, X, Y):
    if len(X) == len(Y):
        print("Yes")
        return
    x0 = X.c("0")
    x1 = X.c("1")
    y0 = Y.c("0")
    y1 = Y.c("1")
    if x1 == y1:  # t一样多
        print("No")
        return
    ls = len(S)
    if ls * (x0 - y0) % (y1 - x1) != 0: # t的长度
        print("No")
        return
    lt = ls * (x0 - y0) // (y1 - x1)
    if lt < 0:
        print("No")
        return
    if lt == 0:
        print("Yes")
        return
    g = gcd(ls, lt)

    rh = RollingHash(S)
    x = rh.get(0, g)
    for i in range(g, len(S), g):
        if x != rh.get(i, i + g):
            print("No")
            return
    print("Yes")

    if S != S[:g] * (ls // g):
        print("No")
    else:
        print("Yes")

for _ in range(int(input())):
    S = input()
    X = input()
    Y = input()
    solve(S, X, Y)
