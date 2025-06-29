'''
887. 鸡蛋掉落
https://leetcode.cn/problems/super-egg-drop/

类似题目还有  两个鸡蛋掉落  ,  375. 猜数字大小 II

'''
from functools import cache
from itertools import count


@cache
def dfs(i, j):
    if i == 0 or j == 0 : return 0
    return dfs(i-1, j) + dfs(i - 1, j - 1) + 1

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        for i in count(1):
            if dfs(i, k) >= n: return i