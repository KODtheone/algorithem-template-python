"""
2024年6月9日13:56:06,
给我一个数组nums, 其中每个数字表示我拥有的一枚硬币
想要知道,我都能获得那些数额
## 这个问题看起来很low ,但是套上一些皮就是 2000+ 的困难题 比如:
https://leetcode.cn/problems/last-stone-weight-ii/description/  1049. 最后一块石头的重量 II  rk:2092
本题添加一个 值小于 s//2的条件就好
https://leetcode.cn/problems/maximum-total-reward-using-operations-ii/description/  3181. 执行操作可获得的最大总奖励 II rk:2688
本题必须使用bit式, set式会超时... 另外需要一个条件 v < x

# 至于需要@cache的 set式需要用frozenset 就是另一个问题了...
"""
# set式  利于离散,速度相对慢
def coin_problem(nums):
    dp = {0}
    for x in nums: dp |= {x + v for v in dp}
    return dp
# O(n)

# bit式
def coin_problem(nums):
    dp = 1
    for x in nums: dp |= dp << x
    # return bin(dp)
    #bit式的位表示在位里面, 可以直接看 bin(dp) 但也不是很清楚.  下面换回数组形式
    res = [x for x in range(dp.bit_length()) if dp & 1 << x]
    return res

# 测试
nums = [1,1,2,3]
nums = [1,1,2,999]
print(coin_problem(nums))

# 变体
##  注意为了避免RuntimeError: Set changed size during iteration,  需要先加list()来固化一下每次的枚举
### 在特殊题有用,比如这里:  https://leetcode.cn/problems/tallest-billboard/description/ 见笔记   这道题的 +1 和 -1 是二选一的,所以不能直接|=操作,而是固化之后二选一
def coin_problem(nums):
    dp = {0}
    for x in nums:
        for v in list(dp):
            dp.add(v+x)
    return dp
