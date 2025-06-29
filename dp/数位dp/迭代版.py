'''
例题: https://atcoder.jp/contests/abc336/submissions/49324916
E - Digit Sum Divisible
#注意,这个版的常数取太大了  导致cpy会超时, pypy可以过...
'''
N = [*map(int,input())]
ans = 0
for s in range(1,127):
    dp = [[[[0,0] for m in range(s)] for i in range(s+1)] for d in range(len(N)+1)]
    dp[0][0][0][1] = 1
    for d in range(len(N)):
        for i in range(s+1):
            for m in range(s):
                for f in range(2):
                    for t in range(10):
                        if i+t > s or ( f and N[d]<t ) : continue
                        dp[d+1][i+t][(m*10+t)%s][int(f and N[d]==t)] += dp[d][i][m][f]
    ans += sum(dp[len(N)][s][0])
print(ans)

"""
更好的版本
"""
standard_input, packages, output_together = 1, 1, 1
dfs, hashing, read_from_file = 0, 0, 0
de = 1

if 1:

    if standard_input:
        import io, os, sys

        input = lambda: sys.stdin.readline().strip()

        inf = float('inf')


        def I():
            return input()


        def II():
            return int(input())


        def MII():
            return map(int, input().split())


        def LI():
            return list(input().split())


        def LII():
            return list(map(int, input().split()))


        def LFI():
            return list(map(float, input().split()))


        def GMI():
            return map(lambda x: int(x) - 1, input().split())


        def LGMI():
            return list(map(lambda x: int(x) - 1, input().split()))

    if packages:
        from io import BytesIO, IOBase
        import math

        import random
        import os

        import bisect
        import typing
        from collections import Counter, defaultdict, deque
        from copy import deepcopy
        from functools import cmp_to_key, lru_cache, reduce
        from heapq import merge, heapify, heappop, heappush, heappushpop, nlargest, nsmallest
        from itertools import accumulate, combinations, permutations, count, product
        from operator import add, iand, ior, itemgetter, mul, xor
        from string import ascii_lowercase, ascii_uppercase, ascii_letters
        from typing import *

        BUFSIZE = 4096

    if output_together:
        class FastIO(IOBase):
            newlines = 0

            def __init__(self, file):
                self._fd = file.fileno()
                self.buffer = BytesIO()
                self.writable = "x" in file.mode or "r" not in file.mode
                self.write = self.buffer.write if self.writable else None

            def read(self):
                while True:
                    b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                    if not b:
                        break
                    ptr = self.buffer.tell()
                    self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
                self.newlines = 0
                return self.buffer.read()

            def readline(self):
                while self.newlines == 0:
                    b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                    self.newlines = b.count(b"\n") + (not b)
                    ptr = self.buffer.tell()
                    self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
                self.newlines -= 1
                return self.buffer.readline()

            def flush(self):
                if self.writable:
                    os.write(self._fd, self.buffer.getvalue())
                    self.buffer.truncate(0), self.buffer.seek(0)


        class IOWrapper(IOBase):
            def __init__(self, file):
                self.buffer = FastIO(file)
                self.flush = self.buffer.flush
                self.writable = self.buffer.writable
                self.write = lambda s: self.buffer.write(s.encode("ascii"))
                self.read = lambda: self.buffer.read().decode("ascii")
                self.readline = lambda: self.buffer.readline().decode("ascii")


        sys.stdout = IOWrapper(sys.stdout)

    if dfs:
        from types import GeneratorType


        def bootstrap(f, stack=[]):
            def wrappedfunc(*args, **kwargs):
                if stack:
                    return f(*args, **kwargs)
                else:
                    to = f(*args, **kwargs)
                    while True:
                        if type(to) is GeneratorType:
                            stack.append(to)
                            to = next(to)
                        else:
                            stack.pop()
                            if not stack:
                                break
                            to = stack[-1].send(to)
                    return to

            return wrappedfunc

    if hashing:
        RANDOM = random.getrandbits(20)


        class Wrapper(int):
            def __init__(self, x):
                int.__init__(x)

            def __hash__(self):
                return super(Wrapper, self).__hash__() ^ RANDOM

    if read_from_file:
        file = open("input.txt", "r").readline().strip()[1:-1]
        fin = open(file, 'r')
        input = lambda: fin.readline().strip()
        output_file = open("output.txt", "w")


        def fprint(*args, **kwargs):
            print(*args, **kwargs, file=output_file)

    if de:
        def debug(*args, **kwargs):
            print('\033[92m', end='')
            print(*args, **kwargs)
            print('\033[0m', end='')


def main():
    n = II()
    n += 1

    val = [int(x) for x in str(n)]

    def calc(digit_sum):
        dp = [[0] * digit_sum for _ in range(digit_sum + 1)]

        x_mod = x_sum = 0

        for i in range(len(val)):

            ndp = [[0] * digit_sum for _ in range(digit_sum + 1)]
            for cur_sum in range(digit_sum + 1):
                for cur_mod in range(digit_sum):
                    if dp[cur_sum][cur_mod]:
                        for new_digit in range(10):
                            if cur_sum + new_digit <= digit_sum:
                                ndp[cur_sum + new_digit][(cur_mod * 10 + new_digit) % digit_sum] += dp[cur_sum][cur_mod]

            for new_digit in range(val[i]):
                if x_sum + new_digit <= digit_sum:
                    ndp[x_sum + new_digit][(x_mod * 10 + new_digit) % digit_sum] += 1

            x_sum += val[i]
            x_mod = x_mod * 10 + val[i]
            dp = ndp
        return dp[digit_sum][0]

    ans = 0
    for digit_sum in range(1, 140):
        ans += calc(digit_sum)
    print(ans)
    return


t = 1
for _ in range(t):
    main()