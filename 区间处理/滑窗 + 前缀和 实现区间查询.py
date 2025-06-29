'''
例题: 3261. 统计满足 K 约束的子字符串数量 II
https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii/description/
原理:  因为要进行区间查询,  从l到某一点[l,r]内某一点j, [l,j]是完全满足的,  而[j + 1, r]区间中满足条件的个数可以用前缀和优化.   预处理的时候,可以同时知道right[l] 代表从l开始全满足的最远点,  还有 pre_sum[r] 表示以r为终点的前缀和


'''
from collections import defaultdict
from typing import List


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        c = defaultdict(int)
        l = 0
        n = len(s)
        right = [n] * n
        pre = [0]
        for r, x in enumerate(s):
            c[x] += 1
            while c["0"] > k < c["1"]:  # 这一步替换为你的判断条件
                c[s[l]] -= 1
                right[l] = r - 1
                l += 1
            pre += pre[-1] + r - l + 1,
        ans = []
        for l, r in queries:
            j = min(right[l], r)
            ans += pre[r + 1] - pre[j +1] + (j - l + 1)*(j - l + 2) // 2 ,
        return ans


# 纯享版
# 输入: 01串 s, 条件: 连续子串中的0和1不能同时大于k,  queries: 区间查询
# 输出: 每个区间内满足条件的子串个数
def fun(s: str, k: int, queries) :
    c = defaultdict(int)
    l = 0
    n = len(s)
    right = [n] * n
    pre = [0]
    for r, x in enumerate(s):
        c[x] += 1
        while c["0"] > k < c["1"]:  # 这一步替换为你的判断条件(取否)
            c[s[l]] -= 1
            right[l] = r - 1
            l += 1
        pre += pre[-1] + r - l + 1,
    ans = []
    for l, r in queries:
        j = min(right[l], r)
        ans += pre[r + 1] - pre[j +1] + (j - l + 1)*(j - l + 2) // 2 ,
    return ans


s = "0001111"
k = 2
queries = [[0,6]]
print(fun(s, k, queries))