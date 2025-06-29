'''
from: https://leetcode.cn/problems/number-of-pairs-satisfying-inequality/solutions/1863557/by-endlesscheng-9prc/
树状数组(binary indexed tree,发明者Peter M.Fenwick 1994)

'''


# bit作为一个通用的储存结构.    这道题里,可以用SortedList替换
##注意! 离散化之后 x要从1开始 , 而不是从0 开始
class BIT:
    def __init__(self, n):
        self.tree = [0] * n

    def add(self, x):
        while x < len(self.tree):
            self.tree[x] += 1  #这里默认加1了, 可以自己写想加几
            x += x & -x

    def query(self, x):
        res = 0
        while x > 0:
            res += self.tree[x]
            x &= x - 1
        return res


'''
一个经典例子 ,  可以当做是SortedList, 同样适用
例题: https://leetcode.cn/problems/count-of-smaller-numbers-after-self/
'''


class BIT:
    def __init__(self, n):
        self.tree = [0] * n

    def add(self, x):
        while x < len(self.tree):
            self.tree[x] += 1   #这里默认加1了, 可以自己写想加几
            x += x & -x

    def query(self, x):     #query的本意是求和的;配合后面bit.query(mp[nums[i]] - 1),意思是寻找更小的位置的和, 等价于 在SortedList二分找小于自己的元素的个数
        res = 0
        while x > 0:
            res += self.tree[x]
            x &= x - 1
        return res

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        j = 1
        mp = {}
        for x in sorted(nums):  # 离散化  ##注意! 离散化之后 x要从1开始 , 而不是从0 开始
            if x not in mp:
                mp[x] = j
                j += 1

        bit = BIT(j)
        for i in range(n - 1, -1, -1):
            cnt = bit.query(mp[nums[i]] - 1)
            ans[i] = cnt
            bit.add(mp[nums[i]])
        return ans
