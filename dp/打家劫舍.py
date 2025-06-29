"""
2024年6月23日22:34:21, 经典题目
https://leetcode.cn/problems/Gu0c2T/description/

"""

# 输入:  nums:一个数字列表
# 输出: 不带任何相邻取值的 最大总取值数
def rob(nums) -> int:
    f0 = f1 = 0
    for x in nums:  f0, f1 = f1, max(f1, f0 + x)
    return f1

# O(!n)