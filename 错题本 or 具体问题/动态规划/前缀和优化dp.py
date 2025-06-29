'''
2024年8月13日10:04:34,  https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-ii/submissions/554277539/
3251. 单调数组对的数目 II

前缀和优化, prefix sum的计算和下一个循环是并列的,所以不在增加复杂度
2024年11月28日09:12:24,  神奇巧妙的算法   组合数学!
https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-ii/solutions/2876190/qian-zhui-he-you-hua-dppythonjavacgo-by-3biek/

看起来像是 : 上台阶
上台阶, 向右走n步, 向上走m步, 总共n+m步, 从n+m步中选出n步, 即C(n+m, n)
如果连续的台阶, b - a > 0  则说明这一阶必要要上 b - a 步, 要从m中减去

'''
from itertools import pairwise
from math import comb
from typing import List


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10**9+7
        m = nums[-1]
        n = len(nums)
        d = sum(max(b - a, 0) for a, b in pairwise(nums))
        return comb(max(n + m -d, 0), n) % mod
