'''
题目:2576. 求出最多标记下标   https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/description/
大意,给一个数组, 从数组中标记最多2 * nums[i] <= nums[j]

方法,贪心,  从中间开始找  最大的k个数 和最小的k个数能配对(顺序的)  (二分方法)
更简单的, 顺序指针方法


'''

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        mid = (len(nums) + 1) // 2
        i = 0
        for x in nums[mid:]:
            if nums[i] <= x//2:
                i += 1
        return i * 2