'''
2024年12月15日20:45:47
LCP 数组  最长公共前缀（Longest Common Prefix）
https://leetcode.cn/problems/count-beautiful-splits-in-an-array/solutions/3020939/liang-chong-fang-fa-lcp-shu-zu-z-shu-zu-dwbrd/

'''
from typing import List


class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i - 1, -1):
                if nums[i] == nums[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1
        # print(lcp)
        ans = 0
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if i <= j - i and lcp[0][i] >= i or j - i <= n - j and lcp[i][j] >= j - i:
                    ans += 1
        return ans
