from typing import List
'''
例题: 56. 合并区间 https://leetcode.cn/problems/merge-intervals/description/
用于将n个可能存在重合的区间整理成最简形式

'''

# 算法的精髓:  用起点排序, 然后逐个找终点,更大的替换成新终点
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # 这里多写上条件, key=lambda x:x[0] 会比不写更快; 虽然本来可以不用写的...
        result = []
        for temp in intervals:
            if not result or result[-1][1] < temp[0]:  result.append(temp)
            else:   result[-1][1] = max(temp[1], result[-1][1])
        return result

# 纯享版
def mg(intervals):
    intervals.sort(key=lambda x: x[0])
    result = []
    for a, b in intervals:
        if not result or result[-1][1] < a:
            result.append([a, b])
        else:
            result[-1][1] = max(b, result[-1][1])
    return result

# 2024年7月19日21:46:08, 原版 ,  for temp in intervals: 这个写法,直接遍历取列表,可能会造成一些意料之外的问题;  生成的列表具有关联性,不是独立的
def mg(intervals):
    intervals.sort(key=lambda x: x[0])
    result = []
    for temp in intervals:
        if not result or result[-1][1] < temp[0]:   result.append(temp)
        else:    result[-1][1] = max(temp[1], result[-1][1])
    return result