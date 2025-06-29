'''
初级问题: 2335. 装满杯子需要的最短总时长   https://leetcode.cn/problems/minimum-amount-of-time-to-fill-cups/description/?envType=problem-list-v2&envId=c0v1S6X9
(这个是真正的三堆石子)1753. 移除石子的最大得分   https://leetcode.cn/problems/maximum-score-from-removing-stones/description/

终极问题:  3139. 使数组中所有元素相等的最小开销     https://leetcode.cn/problems/minimum-cost-to-equalize-array/description/
# 分类讨论,   画图, 三条直线的交点 , 就可以找到数学解法

'''
class Solution:
    def minCostToEqualizeArray(self, nums: List[int], c1: int, c2: int) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        m = min(nums)
        M = max(nums)
        base = n * M - sum(nums)
        if n <= 2 or c1 * 2 <= c2:
            return base * c1 % MOD

        def f(x: int) -> int:
            s = base + (x - M) * n
            d = x - m
            if d * 2 <= s:
                return s // 2 * c2 + s % 2 * c1
            return (s - d) * c2 + (d * 2 - s) * c1

        i = (n * M - m * 2 - base + n - 3) // (n - 2)
        return min(f(M), f(M + 1)) % MOD if i <= M else \
               min(f(M), f(i - 1), f(i), f(i + 1)) % MOD