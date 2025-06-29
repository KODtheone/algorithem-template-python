'''
2024年5月26日22:42:40, 不得不学习一下线段树了...
另外, 这个数据结构分类,实际上和别的目录有些重合    没错,就是 列表  和 区间那里
不过,我打算使用0x3f的分组法了
# 比较奇怪的问题, 使用build的话,确实要比单个change进去速度快一点...
猜测: build相当于一个段修改

'''
from math import inf
from typing import List

# 问题描述: 给出一个len = n 的数组nums(初始都是0, 若给了nums,则enumerate并修改值) 需要两种操作:1, 修改index上的值  2,查询[l,r]区间内的最大值
# 纯享版  以sum为例:
class SegmentTree:
    def __init__(self, n: List[int]):
        self.x = [0] * (t := 2 << n.bit_length())

    def change(self, index: int, val: int, node: int, s: int, e: int):
        if s == e:
            self.x[node] = val
            return
        m = s + (e - s) // 2
        if index <= m:   self.change(index, val, node * 2 + 1, s, m)
        else:            self.change(index, val, node * 2 + 2, m + 1, e)
        self.x[node] = self.x[node * 2 + 1] + self.x[node * 2 + 2]

    def query_x(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left <= s and right >= e:     return self.x[node]
        x = 0
        m = s + (e - s) // 2
        if right > m:   x += self.query_x(left, right, node * 2 + 2, m + 1, e)
        if left <= m:   x += self.query_x(left, right, node * 2 + 1, s, m)
        return x

# ##   修改为 max
#     def range_max(self, left: int, right: int, node: int, s: int, e: int) -> int:
#         if left <= s and right >= e:     return self.max[node]
#         mx = - inf
#         m = s + (e - s) // 2
#         if right > m:   mx = max(mx, self.range_max(left, right, node * 2 + 2, m + 1, e))
#         if left <= m:   mx = max(mx, self.range_max(left, right, node * 2 + 1, s, m))
#         return mx

nums = [1,2,3,4,5,6,7]
e = len(nums) - 1
st = SegmentTree(len(nums))   # 实例化
for i, x in enumerate(nums):  # 相当于之前的build 录入数组
    st.change(i,x,0,0,e)
print(st.x)
print(st.range_sum(0,2, 0, 0, e))    # 0, 0 , e 是半固定值, 固定的递归入口,但是递归时值就变化了
st.change(0,-2,0,0,e)
print(st.range_sum(0,1, 0, 0, e))
print(st.range_sum(0,0, 0, 0, e))

# 基础线段树; 功能:  给出一个数组 nums , 更新: 修改nums[i]的值  查询: 查询nums[l:r+1] 的 1, sum, 2, max 3,min
# 2024年5月28日13:40:10, sum max min的功能似乎没法融为一体, 因为在build里面就有区别了
# 2024年5月28日15:09:24, build 可以不要,因为build的本质就是 enumerate(nums) 进行单个值的修改; 因此总体的build可以拆掉
# sum 用: ( index 从0开始)
class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.seg = [0] * (2 << n.bit_length())
        self.build(nums, 0, 0, n - 1)

    def build(self, nums: List[int], node: int, s: int, e: int):
        if s == e:
            self.seg[node] = nums[s]
            return
        m = s + (e - s) // 2
        self.build(nums, node * 2 + 1, s, m)
        self.build(nums, node * 2 + 2, m + 1, e)
        self.seg[node] = self.seg[node * 2 + 1] + self.seg[node * 2 + 2]

    def change(self, index: int, val: int, node: int, s: int, e: int):
        if s == e:
            self.seg[node] = val
            return
        m = s + (e - s) // 2
        if index <= m:
            self.change(index, val, node * 2 + 1, s, m)
        else:
            self.change(index, val, node * 2 + 2, m + 1, e)
        self.seg[node] = self.seg[node * 2 + 1] + self.seg[node * 2 + 2]

    def range_sum(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:
            return self.seg[node]
        m = s + (e - s) // 2
        if right <= m:
            return self.range_sum(left, right, node * 2 + 1, s, m)
        if left > m:
            return self.range_sum(left, right, node * 2 + 2, m + 1, e)
        return self.range_sum(left, m, node * 2 + 1, s, m) + self.range_sum(m + 1, right, node * 2 + 2, m + 1, e)
# SegmentTree class 使用方法:
nums = [1,2,3,4,5,6,7]
e = len(nums) - 1
st = SegmentTree(nums)   # 实例化
print(st.seg)
print(st.range_sum(0,2, 0, 0, e))    # 0, 0 , e 是半固定值, 固定的递归入口,但是递归时值就变化了
st.change(0,-2,0,0,e)
print(st.range_sum(0,1, 0, 0, e))
print(st.range_sum(0,0, 0, 0, e))
print(st.seg)

## 记录最大值
class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.seg = [0] * (2 << n.bit_length())
        self.build(nums, 0, 0, n - 1)

    def build(self, nums: List[int], node: int, s: int, e: int):
        if s == e:
            self.seg[node] = nums[s]
            return
        m = s + (e - s) // 2
        self.build(nums, node * 2 + 1, s, m)
        self.build(nums, node * 2 + 2, m + 1, e)
        self.seg[node] = max(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def change(self, index: int, val: int, node: int, s: int, e: int):
        if s == e:
            self.seg[node] = val
            return
        m = s + (e - s) // 2
        if index <= m:
            self.change(index, val, node * 2 + 1, s, m)
        else:
            self.change(index, val, node * 2 + 2, m + 1, e)
        self.seg[node] = max(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def range_max(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:
            return self.seg[node]
        m = s + (e - s) // 2
        if right <= m:
            return self.range_max(left, right, node * 2 + 1, s, m)
        if left > m:
            return self.range_max(left, right, node * 2 + 2, m + 1, e)
        return max(self.range_max(left, m, node * 2 + 1, s, m), self.range_max(m + 1, right, node * 2 + 2, m + 1, e))


## 记录最小值
class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.seg = [0] * (2 << n.bit_length())
        self.build(nums, 0, 0, n - 1)

    def build(self, nums: List[int], node: int, s: int, e: int):
        if s == e:
            self.seg[node] = nums[s]
            return
        m = s + (e - s) // 2
        self.build(nums, node * 2 + 1, s, m)
        self.build(nums, node * 2 + 2, m + 1, e)
        self.seg[node] = min(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def change(self, index: int, val: int, node: int, s: int, e: int):
        if s == e:
            self.seg[node] = val
            return
        m = s + (e - s) // 2
        if index <= m:
            self.change(index, val, node * 2 + 1, s, m)
        else:
            self.change(index, val, node * 2 + 2, m + 1, e)
        self.seg[node] = min(self.seg[node * 2 + 1], self.seg[node * 2 + 2])

    def range_min(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:
            return self.seg[node]
        m = s + (e - s) // 2
        if right <= m:
            return self.range_min(left, right, node * 2 + 1, s, m)
        if left > m:
            return self.range_min(left, right, node * 2 + 2, m + 1, e)
        return min(self.range_min(left, m, node * 2 + 1, s, m), self.range_min(m + 1, right, node * 2 + 2, m + 1, e))

## 终极综合版 ##但是注意!  这个会有三倍的时间... 因为三个属性同是都计算出来了...
# 2024年8月7日14:55:34, 这种综合方式是错的, 正确的应该是 把计算方式 op当做参数传进去...
class SegmentTree:
    def __init__(self, n: List[int]):
        self.sum = [0] * (t := 2 << n.bit_length())
        self.max = [0] * t
        self.min = [0] * t

    def change(self, index: int, val: int, node: int, s: int, e: int):
        if s == e:
            self.sum[node] = val
            self.max[node] = val
            self.min[node] = val
            return
        m = s + (e - s) // 2
        if index <= m:   self.change(index, val, node * 2 + 1, s, m)
        else:            self.change(index, val, node * 2 + 2, m + 1, e)
        self.sum[node] = self.sum[node * 2 + 1] + self.sum[node * 2 + 2]
        self.max[node] = max(self.max[node * 2 + 1], self.max[node * 2 + 2])
        self.min[node] = min(self.min[node * 2 + 1], self.min[node * 2 + 2])

    def range_sum(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:     return self.sum[node]
        m = s + (e - s) // 2
        if right <= m:   return self.range_sum(left, right, node * 2 + 1, s, m)
        if left > m:     return self.range_sum(left, right, node * 2 + 2, m + 1, e)
        return self.range_sum(left, m, node * 2 + 1, s, m) + self.range_sum(m + 1, right, node * 2 + 2, m + 1, e)

    def range_max(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:     return self.max[node]
        m = s + (e - s) // 2
        if right <= m:    return self.range_max(left, right, node * 2 + 1, s, m)
        if left > m:      return self.range_max(left, right, node * 2 + 2, m + 1, e)
        return max(self.range_max(left, m, node * 2 + 1, s, m), self.range_max(m + 1, right, node * 2 + 2, m + 1, e))

    def range_min(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:     return self.min[node]
        m = s + (e - s) // 2
        if right <= m:    return self.range_min(left, right, node * 2 + 1, s, m)
        if left > m:      return self.range_min(left, right, node * 2 + 2, m + 1, e)
        return min(self.range_min(left, m, node * 2 + 1, s, m), self.range_min(m + 1, right, node * 2 + 2, m + 1, e))
# SegmentTree class 使用方法:
nums = [1,2,3,4,5,6,7]
e = len(nums) - 1
st = SegmentTree(len(nums))   # 实例化
for i, x in enumerate(nums):  # 相当于之前的build 录入数组
    st.change(i,x,0,0,e)
print(st.max)
print(st.range_max(1,5,0,0,e))
print(st.range_min(0,5,0,0,e))
print(st.range_sum(0,2, 0, 0, e))    # 0, 0 , e 是半固定值, 固定的递归入口,但是递归时值就变化了
st.change(0,-2,0,0,e)
print(st.range_sum(0,1, 0, 0, e))
print(st.range_sum(0,0, 0, 0, e))
print(st.min)
print(st.range_min(0,5,0,0,e))
print(st.range_min(1,5,0,0,e))


