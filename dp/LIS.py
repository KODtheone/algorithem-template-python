'''
LIS系列问题: 最长递增子序列 Longest Increasing Subsequence (LIS)
dp n^2   利用数据结构可以优化到nlogn
更加完整的问题, 在统计递增长度的同时 ,统计情况个数
例题:https://www.geeksforgeeks.org/count-number-increasing-subsequences-size-k/?ref=gcse_ind
Count number of increasing subsequences of size k     统计长为k的is的个数
另一个可以参考的方法题解:  https://leetcode.cn/problems/number-of-longest-increasing-subsequence/solutions/1007341/gong-shui-san-xie-lis-de-fang-an-shu-wen-obuz/
明显nlogn更好, 所以优先掌握 线段树优化的方法

2024年9月10日16:29:23, 板子很好用,但是原理我还没有仔细看...


'''
from bisect import *
from typing import *



# 最朴素版本:  计算lis的长度:
def LIS(nums):
    stack = []
    for num in nums:
        idx = bisect_left(stack, num)
        if idx < len(stack):
            stack[idx] = num
        else:
            stack.append(num)
    return len(stack)
'''
应用  看似二维排序, 其实可以转换成 lis:  https://leetcode.cn/problems/length-of-the-longest-increasing-path/description/
注意, 给排序加上个限制 ncs.sort(key=lambda p: (p[0], -p[1]))

'''


# 长度为k的 is 的情况数
tree = []

def segtree(arr: List[int]) -> int:
    n = len(arr)
    temp = arr.copy()
    temp.sort()
    mpp = {}
    mx = 0
    for i in range(n):
        if temp[i] not in mpp:
            mpp[temp[i]] = mx
            mx += 1
    for i in range(n):
        arr[i] = mpp[arr[i]]
    return mx

def summation(left: List[int], right: List[int], k: int) -> List[int]:
    res = [0] * (k + 1)
    for i in range(1, k + 1):
        res[i] = left[i] + right[i]
    return res

def query(start: int, end: int, parent: int, qstart: int, qend: int, k: int) -> List[int]:
    if end < qstart or qend < start:
        return [0] * (k + 1)
    if qstart <= start and qend >= end:
        return tree[parent]
    mid = (start + end) // 2
    left = query(start, mid, 2 * parent + 1, qstart, qend, k)
    right = query(mid + 1, end, 2 * parent + 2, qstart, qend, k)
    return summation(left, right, k)

def update(start: int, end: int, parent: int, index: int, updateThis: List[int], k: int) -> None:
    if index < start or index > end:
        return
    if start == end:
        tree[parent] = summation(updateThis, tree[parent], k)
        return
    mid = (start + end) // 2
    if index > mid:
        update(mid + 1, end, 2 * parent + 2, index, updateThis, k)
    else:
        update(start, mid, 2 * parent + 1, index, updateThis, k)
    left = tree[2 * parent + 1]
    right = tree[2 * parent + 2]
    tree[parent] = summation(left, right, k)
    return

def numOfIncSubseqOfSizeK(arr: List[int], K: int) -> int:
    n = len(arr)
    mx = segtree(arr)
    global tree
    tree = [[0] * (K + 1) for _ in range(4 * mx + 1)]
    for i in range(n):
        Kj = [0] * (K + 1)
        Kj[1] = 1
        if arr[i] > 0:
            Ki = query(0, mx, 0, 0, arr[i] - 1, K)
            for k in range(2, K + 1):
                Kj[k] = Ki[k - 1]
        update(0, mx, 0, arr[i], Kj, K)
    print(tree[0])
    return tree[0][K]


if __name__ == '__main__':
    arr = [2,2,2,2]
    # k = 3
    # print("Number of Increasing Subsequences of size", k, "=", numOfIncSubseqOfSizeK(arr, k))
    for k in range(1, len(arr) + 1):
        print("Number of Increasing Subsequences of size", k, "=", numOfIncSubseqOfSizeK(arr, k))


'''
lis的情况数
https://www.geeksforgeeks.org/number-of-longest-increasing-subsequences/?ref=header_outind
'''
# O(n^2) 实现
def countLIS(arr):
    n = len(arr)
    lis = [1] * n
    count = [1] * n
    max_len = 1
    for i in range(1, n):
        for prev in range(i):
            if arr[i] > arr[prev]:
                if lis[i] < lis[prev] + 1:
                    lis[i] = lis[prev] + 1
                    count[i] = count[prev]
                elif lis[i] == lis[prev] + 1:
                    count[i] += count[prev]
        max_len = max(max_len, lis[i])
    res = sum(count[i] for i in range(n) if lis[i] == max_len)
    return res

# Driver program to test the above function
arr = [10, 10, 10, 10]
print(countLIS(arr))

# O(n log n) 实现
def RANKER(arr):
    n = len(arr)
    temp = arr.copy()
    temp.sort()
    rank = {}
    mx = 0
    for i in range(n):
        if temp[i] not in rank:
            rank[temp[i]] = mx
            mx += 1
    for i in range(n):
        arr[i] = rank[arr[i]]
    return mx

def chooseBest(left, right):
    mxLen_LFT, ways_LFT = left
    mxLen_RHT, ways_RHT = right
    if mxLen_LFT > mxLen_RHT:
        res = (mxLen_LFT, ways_LFT)
    elif mxLen_LFT < mxLen_RHT:
        res = (mxLen_RHT, ways_RHT)
    else:
        res = (mxLen_LFT, ways_LFT + ways_RHT)
    return res

def update(start, end, parent, element, mxLength, ways, tree):
    if start == end:
        if tree[parent][0] == mxLength:
            tree[parent] = (mxLength, tree[parent][1] + ways)
        else:
            tree[parent] = (mxLength, ways)
        return
    mid = (start + end) // 2
    if element <= mid:
        update(start, mid, 2 * parent + 1, element, mxLength, ways, tree)
    else:
        update(mid + 1, end, 2 * parent + 2, element, mxLength, ways, tree)
    tree[parent] = chooseBest(tree[2 * parent + 1], tree[2 * parent + 2])

def maxLen(start, end, qstart, qend, parent, tree):
    if start > qend or end < qstart:
        return (0, 0)
    if start >= qstart and end <= qend:
        return tree[parent]
    mid = (start + end) // 2
    left = maxLen(start, mid, qstart, qend, 2 * parent + 1, tree)
    right = maxLen(mid + 1, end, qstart, qend, 2 * parent + 2, tree)
    return chooseBest(left, right)

def findNumberOfLIS(arr):
    n = len(arr)
    mx = RANKER(arr)
    tree = [(0, 0)] * (4 * mx + 5)
    for i in range(n):
        mxLen = 1
        ways = 1
        if arr[i] > 0:
            info = maxLen(0, mx, 0, arr[i] - 1, 0, tree)
            if info[0] + 1 > mxLen:
                mxLen = info[0] + 1
                ways = info[1]
        update(0, mx, 0, arr[i], mxLen, ways, tree)
    return tree[0][1]


# Example usage
arr = [1, 3, 5, 4, 7]
print(findNumberOfLIS(arr))  # output: 2
