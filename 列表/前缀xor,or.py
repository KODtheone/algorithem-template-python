'''
使用例题: https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/description/
尝试使用但tle的例题: https://codeforces.com/contest/1957/problem/D
但是,单纯用来查询一段数字的xor值应该是没问题的 毕竟是 O(log(max(nums)) * n ) 约等于 O(n)    时间会比较微妙

2024年5月15日10:02:06,发现有问题啊,  xor的话,似乎可以直接对标前缀和来计算的...

'''


# 功能 : 给出数列nums, 用前缀和的方式计算前缀xor值, 以达到在O(1)的时间查询[a,b]段xor值的结果
# 因为nums中最大数字范围为10**9, 因此 ps 中的每个单元需要 30位,  2**10 = 1024 ~ 10**3, 2**30 ~ 10**9
# 时间复杂度 预处理: O(n) ~ O(log(max(nums)) * n ) 查询: O(log(max(nums))) ~ O(1)
# 参数:  建class:  nums;  查询:  l,r  返回[l,r]区间xor的结果
class Xor_ps():
    def __init__(self, nums):
        self.ps = [[0] * 30]
        for x in nums:
            t = self.ps[-1].copy()
            i = 0
            while x:
                if x & 1:
                    t[i] += 1
                x >>= 1
                i += 1
            self.ps.append(t)

    def query(self, a, b):
        ans = 0
        for i in range(30):
            if (self.ps[b + 1][i] - self.ps[a][i]) % 2:
                ans += 1 << i
        return ans
#时间复杂度: O(n * 30) 或者说 O(n * log2(max(nums)))

##对于xor更简单, 同加法的特性
pre_xor = list(accumulate(nums, xor, initial = 0))
# .query(a,b)等价于 pre_xor[b+1]^pre_xor[a]


# 不知道为什么, xor的 if (self.ps[b + 1][i] - self.ps[a][i]) % 2: 判断 比or的 self.ps[b + 1][i] > self.ps[a][i] 判断快很多, 在一个用例(最上例题中的超时提交)上表现为5倍

# or版本, 只要self.ps[b + 1][i] > self.ps[a][i] 即这一位值大于1即可
class Or_ps():
    def __init__(self, nums):
        self.ps = [[0] * 30]
        for x in nums:
            t = self.ps[-1].copy()
            i = 0
            while x:
                if x & 1:
                    t[i] += 1
                x >>= 1
                i += 1
            self.ps.append(t)

    def query(self, a, b):
        ans = 0
        for i in range(30):
            if self.ps[b + 1][i] > self.ps[a][i]:
                ans += 1 << i
        return ans


