'''
2024年11月10日13:30:34
考虑前缀零, 是不是num的

'''

from functools import cache

n = 1111
s = str(n)
@cache
def f(i = 0, is_limit = True, is_num = False) -> int:
    if i == len(s):
        # 或根据题意判断
        return int(is_num)
    res = 0
    if not is_num:
        res = f(i + 1, False, False)
    low = 0 if is_num else 1
    up = int(s[i]) if is_limit else 1
    for d in range(low, up + 1):
        #根据题意的判断
        res += f(i + 1, is_limit and d == up, True)
    return res

print(f(0,True,False))



'''
例题 2024年11月10日13:31:44 
https://leetcode.cn/contest/weekly-contest-423/problems/count-k-reducible-numbers-less-than-n/

'''
dic = [0] * 801
for x in range(2, 801):
    dic[x] = 1 + dic[x.bit_count()]

class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dp(i=0, c=0, is_limit=True, is_num=False) -> int:
            if i == len(s):
                return dic[c] + 1 <= k
            res = 0
            if not is_num:
                res = dp(i + 1, c, False, False)
            low = 0 if is_num else 1
            up = int(s[i]) if is_limit else 1
            for d in range(low, up + 1):
                res += dp(i + 1, c + d, is_limit and d == up, True)
            return res

        return (dp(0, 0, True, False) - (dic[s.count('1')] + 1 <= k ) ) % MOD - 1