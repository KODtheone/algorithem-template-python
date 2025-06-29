'''
问题: https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-ii/submissions/531091272/   3130. 找出所有稳定的二进制数组 II & 3129. 找出所有稳定的二进制数组 I
简述:  给你 a 个 0, b 个1 , 试求 其中连续的0或1都不超过l 个的所有不同排列个数
基本解法:  dfs解  注意  题解中dfs(i,j,k) i,j是剩余要填的个数  而k是最后一位 (i+j这一位)填入的数字


'''
from functools import cache

# 此答案解法:  在dfs中顺路的利用容斥, 排除掉不行的情况   而 负负得正, 不行的情况中不行的情况又加了回来
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10 ** 9 + 7

        @cache
        def dfs(i, j):
            if i == 0: return 0
            if j == 0: return 1 if i <= limit else 0
            return (dfs(i - 1, j) + dfs(j, i - 1) - (dfs(j, i - limit - 1) if i > limit else 0)) % mod

        ans = dfs(zero, one) + dfs(one, zero)
        dfs.cache_clear()
        return ans % mod