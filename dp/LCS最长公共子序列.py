'''
例题:  https://leetcode.cn/problems/longest-common-subsequence/  1143. 最长公共子序列

longest common subsequence

'''
from bisect import bisect_left
from collections import defaultdict

# 说明,  candidate 之中, 保存了 s2的字符转化成 s1中的出现顺序
'''例如 : 
s1 = "abbaa"
s2 = "aba"
candidates = [4, 3, 0, 2, 1, 4, 3, 0]
根据s1,  s1 = [4 ,3 ,0]  s2 = [2,1]
所以, candidates = s1 + s2 + s2 =  [4, 3, 0, 2, 1, 4, 3, 0]
'''
# 最强模版
def LCS(s1, s2):
    m = len(s1)
    hashmap = defaultdict(list)
    for i in range(m - 1, -1, -1):
        hashmap[s1[i]].append(i)
    candidates = []
    for c in s2:
        if c in hashmap:
            candidates.extend(hashmap[c])
    return LIS(candidates)

def LIS(candidates):
    stack = []
    for num in candidates:
        idx = bisect_left(stack, num)
        if idx < len(stack):
            stack[idx] = num
        else:
            stack.append(num)
    return len(stack)

## 利用了lis  最长递增子序列

# 2024年10月25日22:44:03
# 纯享版
def LCS(s1, s2):
    m = len(s1)
    h = defaultdict(list)
    for i in range(m - 1, -1, -1):
        h[s1[i]] += i,
    cs = []
    for c in s2:
        if c in h:
            cs.extend(h[c])
    return LIS(cs)

def LIS(cs):
    st = []
    for num in cs:
        idx = bisect_left(st, num)
        if idx < len(st):
            st[idx] = num
        else:
            st.append(num)
    return len(st)