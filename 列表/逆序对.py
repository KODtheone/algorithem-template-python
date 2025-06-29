"""
例题: 如 https://ac.nowcoder.com/acm/contest/73854/G
这里记录基本型,最快的
input: 一个列表
output:逆序对的个数

reversePairs
2024年7月8日20:06:15,  相邻两项两两交换操作x次,可以落实到逆序对上
例题:https://codeforces.com/contest/1983/problem/D
1, 同间隔的操作可以转化成多次相邻的操作   2,相邻操作一共进行偶数次   3,操作数等于逆序对数目
#前置条件, array里的数distinct,  不然直接yes
"""

from sortedcontainers import SortedList

def r(record) -> int:
    n = len(record)
    sl = SortedList()
    ans = 0
    for i in range(n - 1, -1, -1):
        cnt = sl.bisect_left(record[i])
        ans += cnt
        sl.add(record[i])
    return ans

test = [9, 7, 5, 4, 6]
print(r(test))

#方法二 用bit的 , 防止不能用sl的情况
class BIT:
    def __init__(self, n):
        self.tree = [0] * n

    def add(self, x, v):
        while x < len(self.tree):
            self.tree[x] += v   #这里默认加1了, 可以自己写想加几
            x += x & -x

    def query(self, x):     #query的本意是求和的;配合后面bit.query(mp[nums[i]] - 1),意思是寻找更小的位置的和, 等价于 在SortedList二分找小于自己的元素的个数
        res = 0
        while x > 0:
            res += self.tree[x]
            x &= x - 1
        return res

def reversePairs2(record) -> int:
    t = sorted(list(set(record)))
    # print(t)
    d = {}
    for i, x in enumerate(t):
        d[x] = i
    # print(d)  #{4: 0, 5: 1, 6: 2, 7: 3}
    n = len(t)
    bit = BIT(n+1)
    ans = 0
    for x in record[::-1]:
        ans += bit.query(d[x])
        bit.add(d[x]+1,1)
    return ans
print(reversePairs2(test))
