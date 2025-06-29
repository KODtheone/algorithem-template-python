MOD = 10**9 + 7

def solve(num):
    from math import comb
    from collections import Counter, defaultdict
    import sys
    sys.setrecursionlimit(1 << 25)

    N = len(num)
    N_even = (N + 1) // 2  # positions 0,2,...
    N_odd = N // 2  # positions 1,3,...

    c_d = Counter(int(d) for d in num)
    total_sum = sum(int(d) for d in num)

    if total_sum % 2 != 0:
        return 0

    target_sum = total_sum // 2

    # Precompute factorials and inverses
    maxN = N
    factorial = [1] * (maxN + 1)
    inv_factorial = [1] * (maxN + 1)
    for i in range(1, maxN + 1):
        factorial[i] = factorial[i - 1] * i % MOD

    inv_factorial[maxN] = pow(factorial[maxN], MOD - 2, MOD)
    for i in range(maxN, 0, -1):
        inv_factorial[i - 1] = inv_factorial[i] * i % MOD

    ans = 0
    digits = list(range(10))
    c_d_list = [c_d.get(d, 0) for d in digits]

    memo = {}

    def dfs(pos, count_even, sum_even, counts_even):
        key = (pos, count_even, sum_even)
        if key in memo:
            return
        memo[key] = True
        if count_even > N_even or sum_even > target_sum:
            return
        if pos == 10:
            if count_even == N_even and sum_even == target_sum:
                counts_odd = [c_d_list[i] - counts_even[i] for i in range(10)]

                ways_even = factorial[N_even]
                for i in range(10):
                    ways_even = ways_even * inv_factorial[counts_even[i]] % MOD

                ways_odd = factorial[N_odd]
                for i in range(10):
                    ways_odd = ways_odd * inv_factorial[counts_odd[i]] % MOD

                total_ways = ways_even * ways_odd % MOD
                nonlocal ans
                ans = (ans + total_ways) % MOD
            return

        max_count = min(c_d_list[pos], N_even - count_even)
        for count in range(max_count + 1):
            counts_even_new = counts_even.copy()
            counts_even_new[pos] += count
            dfs(pos + 1, count_even + count, sum_even + count * digits[pos], counts_even_new)

    counts_even_init = [0]*10
    dfs(0, 0, 0, counts_even_init)

    return ans

# 读取输入并输出答案
num = input().strip()
print(solve(num))