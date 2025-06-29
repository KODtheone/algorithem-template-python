'''
3287. 求出数组中最大序列值
https://leetcode.cn/problems/find-the-maximum-sequence-value-of-array/description/

难点部分:    亦是本题的前半部分
给你一个数字列表nums  现在需要得出一个 整理列表:
f[i] 从 nums中取出i个数组成的子序列, 能得到的所有or值 ( 子序列中所有元素 or 运算 )
pre[j] 值使用nums的前j个元素, 从中取出k个数组成的子序列, 能得到的所有or值

# 感觉是一个挺暴力的,  没什么意思的n^2的解法啊...
'''
from functools import reduce
from operator import or_
# suf运算
nums = [1, 2, 3, 4, 5, 8]
k = 2

mx = reduce(or_, nums)
print(mx)
n = len(nums)
suf = [None] * (n - k + 1)
f = [[False] * (mx + 1) for _ in range(k + 1)]
f[0][0] = True
for i in range(n - 1, k - 1, -1):
    v = nums[i]
    # 注意当 i 比较大的时候，循环次数应和 i 有关，因为更大的 j，对应的 f[j] 全为 False
    for j in range(min(k - 1, n - 1 - i), -1, -1):
        for x, has_x in enumerate(f[j]):
            if has_x:
                f[j + 1][x | v] = True
    if i <= n - k:
        suf[i] = f[k].copy()
print(f)
print(suf)
ansf = []
for x in f:
    t = []
    for i, xx in enumerate(x):
        if xx:
            t.append(i)
    ansf += t,
print(ansf)

anssuf = []
for x in suf:
    t = []
    if x == None: continue
    for i, xx in enumerate(x):
        if xx:
            t.append(i)
    anssuf += t,
print(anssuf)