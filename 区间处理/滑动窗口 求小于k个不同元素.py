"""
2024年5月12日21:38:24
例题: https://leetcode.cn/problems/find-the-median-of-the-uniqueness-array/solutions/2759114/er-fen-da-an-hua-dong-chuang-kou-pythonj-ykg9/
用到了滑窗, 其他地方也有类似写法,所以写个板子
sliding window

"""
from collections import Counter


# 问题: 在数组nums的子数组中, 求不同元素数小于k的子数组总数; 暴力思考, nums长度为n, 枚举
#暴力 错误的
def naive(nums, k):
    n = len(nums)
    ans = 0
    for l in range(n):
        for r in range(l,n):
            if len(set(nums[l:r+1])) < k:
                ans += 1
    return ans

#参数: nums: 数组,  k, 期望的不同元素数要小于k
def sw(nums, k):
    ans = l = 0
    cnt = Counter()
    for r, x in enumerate(nums):
        cnt[x] += 1
        while len(cnt) >= k:
            out = nums[l]
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]
            l += 1
        ans += r - l + 1
    return ans

nums = [1,2,3,4,5,6,7]
k = 2
print(naive(nums, k))
print(sw(nums, k))