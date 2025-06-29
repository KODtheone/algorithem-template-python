'''
例题:https://leetcode.cn/problems/smallest-range-ii/  910. 最小差值 II
题意:  给出一个数组,  其中的每个数都必须 +k 或 -k,  操作后, 使得数组的最大值和最小值的差值最小,  返回这个差值

思路:  贪心
小的数变大, 大的数变小, 扫描变大变小的边界

'''
# x 往前的都是变大,  y 往后的都是变小
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        for x, y in pairwise(nums):
            mx = max(x + k, nums[-1] - k)
            mn = min(nums[0] +k, y - k)
            ans = min(ans, mx - mn)
        return ans

# 纯享版
def fun(nums, k):
    nums.sort()
    ans = nums[-1] - nums[0]
    for x, y in pairwise(nums):
        ans = min(ans, max(x + k, nums[-1] - k) - min(nums[0] + k, y - k))
    return ans