'''
2024年10月25日13:22:10
https://leetcode.cn/problems/sorted-gcd-pair-queries/description/
3312. 查询排序后的最大公约数

核心思路:
类似容斥原理
c = nums中是i倍数的数字
cntGcd[i]=  c(c−1) / 2  −cntGcd[2i]−cntGcd[3i]−⋯
这样就算出了 gcd值为i的数对有多少个
注意 , 倒序枚举 i。  这一点又有点像dp的转移方向问题

'''

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        cnt_x = [0] * (mx + 1)
        for x in nums:
            cnt_x[x] += 1
        cnt_gcd = [0] * (mx + 1)
        for i in range(mx, 0, - 1):
            c = 0
            for j in range(i, mx + 1, i):
                c += cnt_x[j]
                cnt_gcd[i] -= cnt_gcd[j]
            cnt_gcd[i] += c *(c - 1) //2
        ps = list(accumulate(cnt_gcd))
        return [bisect_right(ps, q) for q in queries]