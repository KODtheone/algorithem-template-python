"""
例题 https://codeforces.com/contest/1972/problem/C

问题描述:  给出一个数列 arr,  和一个数值 k,  现在,可以将k任意的加到arr中的元素里, 然后求
1, min(arr)的最大值
2, 达到1中最大值时,最少要使用k中多少值

PS: 木筒效应的出处有问题,但是,这个理论没什么毛病.  对取min问题,就取min来计算就完事了...
"""
from sortedcontainers import SortedList


def Db(arr, k):
    l = 0
    r = max(arr) + k + 1  #最高板
    sl = SortedList(arr)
    ps = [0]  # 前缀和
    for x in sl:
        ps += ps[-1] + x,
    # print(ps)  #[0, 1, 3, 6, 10, 15]

    def check(m):
        idx = sl.bisect_left(m + 1) #得到 sl开始大于m的位置; 则[0:idx] 是需要填补的桶
        s = ps[idx]
        # k + s: k个值 加上 原本的前缀和;  < m * idx 说明小于 补齐之后的 总值,  即,k无法做到补齐 m达不到
        return k + s >= m * idx

    # for  i in range(11):  #首先,检查 check(x)的单调性没问题
    #     print(i, check(i))

    def bs(l = l, r = r):
        while l < r:
            mid = (l + r) >> 1
            if not check(mid):
                r = mid
            else:
                l = mid + 1
            # print(l,r,mid, check(mid))
        return r - 1  #为何 - 1, 因为是从 tttffffff转换的
    return bs()

#test
arr = [1,2,3,4,5]
k = 4
k = 0
# print(Db(arr,k))
for i in range(19):
    print("k=",i, Db(arr, i))
##2024年5月5日15:31:52,  终于测试通过;  #把握重点 check的正确性  然后,需要换成 fffftttttt的形式  而找到的位置是第一个t的index, 因此,如果是从 ttttfffff加not变换的,则需要返回 r - 1


# 纯享版
def Db(arr, k):
    l = 0
    r = max(arr) + k + 1  #最高板
    sl = SortedList(arr)
    ps = [0]
    for x in sl:
        ps += ps[-1] + x,

    def check(m):
        idx = sl.bisect_left(m + 1)
        s = ps[idx]
        return k + s >= m * idx

    def bs(l = l, r = r):
        while l < r:
            mid = (l + r) >> 1
            if not check(mid):
                r = mid
            else:
                l = mid + 1
        return r - 1
    return bs()








