'''
利用或运算的性质 + 通用模板
子数组 OR/AND/GCD/LCM 通用模板
例题: https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/solutions/2716483/zi-shu-zu-orandgcd-tong-yong-mo-ban-pyth-n8xj/

'''
from math import inf
from typing import List
#给出列表nums 和一个值k,  要求: or运算结果大于k的子数组(subarray说明连续)的最短长度(因为or运算越来越大,所以一定是求最短)
def minimumSubarrayLength(nums: List[int], k: int) -> int:
    d = dict()
    ans = inf
    for i, x in enumerate(nums):
        d = {or_ | x: left for or_, left in d.items()}  # 这里很神奇,后边的编号会覆盖前面的, ##因为py是按照生成顺序保存数据的,所以遍历的时候也刚刚好完美覆盖了,即保存的是left更大的结果
        d[x] = i
        for or_, left in d.items():
            if or_ >= k:
                if i - left + 1 < ans:
                    ans = i - left + 1  # 更新
    return ans if ans < inf else -1

#时间复杂度:  因为nums在二进制上长度有限,可以当做常数,故 O(n);   或者写O(n*log(max(nums)))


#纯享版
def msl(nums, k):
    d = dict()
    ans = inf
    for i, x in enumerate(nums):
        d = {or_ | x: left for or_, left in d.items()}
        d[x] = i
        for or_, left in d.items():
            if or_ >= k:
                if i - left + 1 < ans:
                    ans = i - left + 1
    return ans if ans < inf else -1


nums = [2, 2, 1, 1, 1, 1, 1]
k = 3
print(msl(nums, k))