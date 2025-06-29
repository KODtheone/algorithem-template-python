'''
提交于 2024.06.10 11:07
例题:3177. 求出最长好子序列 II   https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-ii/description/
#   如果nums[i]不是 10^9 ,我能直接想到dp, 第一维写nums[i]的值, 然后记录, 以nums[i]值为结尾, 变化了j次的最大长度dp
    也是只有两维.  但是nums[i]太大了, 而 nums的长度实际上最多只有 nums.length 种..
    所以实际上,这个题的第一步是一个离散化处理...
# 本题的分类: 子序列dp,且 相邻相关  (另一种就是 相邻无关 例如 01背包)
# 2024年9月6日10:16:02,  注意 外部记录 这个灵魂步骤, 是问题的关键

'''
from typing import List

#解释: 给我一个数组nums, 和一个数字 k,  求nums中, 改变不超过k次的最长子序列,  例如 1,1,1,1,1, 是改变了0次的,  1,1,2,3 改变了两次
#参数: 数组nums,   最多改变次数: k
def maximumLength(nums: List[int], k: int) -> int:
    d = {v: i for i, v in enumerate(set(nums))}  ##离散化##处理之后, 最多nums.length=5000个值
    nums = [d[v] for v in nums]
    dp = [[0] * (k + 1) for _ in range(len(d))]
    ans = [0] * (k + 2)  # 需要一个外部记录最大值;  使用k+2是为了在转移时,去掉判断 if j:  ; ans[k+1] 是一直没有更新的,即一直=0
    for x in nums:
        for j in range(k, -1, -1):
            dp[x][j] = dp[x][j] + 1 if dp[x][j] + 1 > ans[j - 1] + 1 else ans[j - 1] + 1    # max的复杂形式,为了速度; 但比赛无必要
            if dp[x][j] > ans[j]: ans[j] = dp[x][j]
    return ans[-2]


#纯享版
def ml(nums: List[int], k: int) -> int:
    d = {v: i for i, v in enumerate(set(nums))}
    nums = [d[v] for v in nums]
    dp = [[0] * (k + 1) for _ in range(len(d))]
    ans = [0] * (k + 2)
    for x in nums:
        for j in range(k, -1, -1):
            dp[x][j] = dp[x][j] + 1 if dp[x][j] + 1 > ans[j - 1] + 1 else ans[j - 1] + 1
            if dp[x][j] > ans[j]: ans[j] = dp[x][j]
    return ans[-2]


