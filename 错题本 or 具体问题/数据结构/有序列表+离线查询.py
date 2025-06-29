'''
2024年8月10日12:27:06 https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/solutions/2533058/chi-xian-zui-xiao-dui-pythonjavacgo-by-e-9ewj/?envType=daily-question&envId=2024-08-10
 2940. 找到 Alice 和 Bob 可以相遇的建筑

也可使用线段树树上二分,   用板子非常方便

'''


# 方法讲解:  先把能回答的直接回答了, 剩下 hs[a] >= hs[b] 的 存起来, 存成 (hs[a], idx) 放入 res[b]
# 然后遍历hs, 当经过i后,把res[i]放进sl, 因为i之前查不了结果, 然后遇到比sl[0]中的hs[a]更大的h, 就把sl[0]吐出来, 按照 idx 回答
class Solution:
    def leftmostBuildingQueries(self, hs: List[int], qs: List[List[int]]) -> List[int]:
        ans = [-1] * len(qs)
        res = [[] for i in hs]
        for i, (a, b) in enumerate(qs):
            if a > b : a, b = b, a
            if a == b or hs[b] > hs[a]: ans[i] = b
            else: res[b] += [(hs[a], i)]
        from sortedcontainers import SortedList
        sl = SortedList()
        for i, h in enumerate(hs):
            while sl and sl[0][0] < h:
                ans[sl.pop(0)[1]] = i
            for r in res[i]:
                sl.add(r)
        return ans

# 方法二 线段树模板 树上二分查找  不需要离线回答了
# 用lst模板 2000ms  st模板 1300ms
class Solution:
    def leftmostBuildingQueries(self, hs: List[int], qs: List[List[int]]) -> List[int]:
        fmax = lambda x, y: x if x > y else y
        s = ST(hs, 0, fmax)    # atcoder st模板
        ans = []
        for a, b in qs:
            if a > b: a , b = b, a
            if a == b:          ans += a,
            elif hs[b] > hs[a]: ans += b,
            else:
                t = s.bisect_left(b, lambda x: x > hs[a])
                ans += t if t < len(hs) else -1,
        return ans
