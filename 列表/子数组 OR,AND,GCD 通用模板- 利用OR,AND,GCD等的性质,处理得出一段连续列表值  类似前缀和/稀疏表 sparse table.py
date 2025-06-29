'''
同样来自例题: https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/
肖恩的做法, 感觉这个稀疏表的模板更有普适性
原理参考 :https://zhuanlan.zhihu.com/p/105439034
2024年4月22日15:33:13,发现xor用不了

'''

#其中 data是要导入的数字列表     merge method  是 ior
class SparseTable:
    def __init__(self, data, merge_method):
        self.note = [0] * (len(data) + 1)
        self.merge_method = merge_method
        l, r, v = 1, 2, 0
        while True:
            for i in range(l, r):
                if i >= len(self.note):
                    break
                self.note[i] = v
            else:
                l *= 2
                r *= 2
                v += 1
                continue
            break
        self.ST = [[0] * len(data) for _ in range(self.note[-1]+1)]
        self.ST[0] = data
        for i in range(1, len(self.ST)):
            for j in range(len(data) - (1 << i) + 1):
                self.ST[i][j] = merge_method(self.ST[i-1][j], self.ST[i-1][j + (1 << (i-1))])

    def query(self, l, r):  #根据使用知 [l, r]
        pos = self.note[r-l+1]
        return self.merge_method(self.ST[pos][l], self.ST[pos][r - (1 << pos) + 1])



##完整代码 ,附带后面的模板处理:

class SparseTable:
    def __init__(self, data, merge_method):
        self.note = [0] * (len(data) + 1)
        self.merge_method = merge_method
        l, r, v = 1, 2, 0
        while True:
            for i in range(l, r):
                if i >= len(self.note):
                    break
                self.note[i] = v
            else:
                l *= 2
                r *= 2
                v += 1
                continue
            break
        self.ST = [[0] * len(data) for _ in range(self.note[-1]+1)]
        self.ST[0] = data
        for i in range(1, len(self.ST)):
            for j in range(len(data) - (1 << i) + 1):
                self.ST[i][j] = merge_method(self.ST[i-1][j], self.ST[i-1][j + (1 << (i-1))])

    def query(self, l, r):
        pos = self.note[r-l+1]
        return self.merge_method(self.ST[pos][l], self.ST[pos][r - (1 << pos) + 1])


# reduce 是那个我见过的 连续操作  ior就是 或, 这里必须使用函数名
##iand ior ixor  ixor和 xor 都有,似乎是有区别的,带i的说是inplace修改, 但我实际测试了一下,结果没区别...
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if reduce(ior, nums) < k:
            return -1
        st = SparseTable(nums, ior)
        l = r = 0
        n = len(nums)
        ans = inf
        while l < n:
            while r < n and st.query(l, r) < k:
                r += 1
            if r == n: break
            ans = min(ans, r - l + 1)   #根据查询可知, l, r 是闭区间
            l += 1
            r = max(l, r)
        return ans if ans < inf else -1
