'''
2024年4月8日13:22:16

'''
from math import inf
from typing import List


# 可以全不要, ans初始为0, 不然需要ans = -inf
# 参数:  nums
# 功能: 属于一个数列nums,返回这个数列中最大的子数组之和;  本质是dp
def kadane(nums: List[int]) -> int:
    tem = ans = 0
    #ans = -inf
    for x in nums:
        if tem < 0: tem = 0
        tem += x
        if ans < tem: ans = tem
    return ans

# 变体  返回最大子数组的起始位置和终止位置
def kadane_pos(nums: List[int]):
    tem = ans = start = ns = end = 0
    for i, x in enumerate(nums):
        if tem < 0:
            tem = 0
            ns = i
        tem += x
        if ans < tem:
            ans = tem
            end = i
            start = ns
    return (start, end)
    return (start, end), ans

# 测试
if __name__ == '__main__':
    print(kadane_pos([-2, 1, -3, 4, -1, 2, 1, -5, 4, -1000,5]))
