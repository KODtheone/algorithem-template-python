'''
例题:  3277. 查询子数组最大异或值  https://leetcode.cn/problems/maximum-xor-score-subarray-queries/description/

普通的区间dp  观察计算方式, 得出转移方程
f[i][j] = f[i + 1][j] ^ f[i][j - 1]
mx[i][j] = max(f[i][j], mx[i + 1][j], mx[i][j - 1])

注意: 2024年9月14日22:12:09  这个思考方式很神奇,而且似乎是对的... ###
 因为转移方程  是 i+ 1 到i 所以i需要倒叙枚举
 同理的, j -1 到 j  所以j是正序的...

'''

# 解答
class Solution:
    def maximumSubarrayXor(self, nums: List[int], qs: List[List[int]]) -> List[int]:
        n = len(nums)
        f = [[0] * n for i in range(n)]
        mx =[[0] * n for i in range(n)]
        for i in range(n)[::-1]:
            f[i][i] = mx[i][i] = nums[i]
            for j in range( i + 1, n):
                f[i][j] = f[i + 1][j] ^ f[i][j - 1]
                mx[i][j] = max(f[i][j], mx[i + 1][j], mx[i][j - 1])
        return [mx[i][j] for i, j in qs]