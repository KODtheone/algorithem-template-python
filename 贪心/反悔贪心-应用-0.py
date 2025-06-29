'''
2813. 子序列最大优雅度
https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/solutions/2375128/fan-hui-tan-xin-pythonjavacgo-by-endless-v2w1/
思考过程: 根据价值排序, 先拿价值最高的k个物品, 然后根据种类分类讨论
如果种类已经出现过, 一定不添加,因为价值是减少的
如果种类是新的, 则替换已取k个里面出现过重复的, 并且,一定是替换价值最低的
因此, 要提前用一个stack记录重复种类的item, 因为排序过,所以先进入的大,后进入的小; 替换时直接pop就行了

## 感觉这道题没有体现出反悔来, 不如切披萨那道题直观

2024年10月7日11:13:58,  感觉这个其实应该叫做   单调栈 + 贪心
另一个例题: 871. 最低加油次数
https://leetcode.cn/problems/minimum-number-of-refueling-stops/
有序数组 + 贪心
'''
from typing import List


# 参数: items  二维数组  n x 2 , 第一个数字表示价值, 第二个数字表示种类;   k, 选择其中k个
# 而总价值的计算为 k个物品的价值和  + 总种类数的平方
# 寻扎k个物品的最大总价值
def findMaximumElegance(items: List[List[int]], k: int) -> int:
    items.sort(key = lambda x: -x[0])
    seen = set()
    st = []
    sp = ans = 0
    for i, (a, b) in enumerate(items):
        if i < k:
            if b not in seen:
                seen.add(b)
            else:
                st += [a]
            sp += a
        elif st and b not in seen:
            seen.add(b)
            sp += a - st.pop()
        ans = max(ans, sp + len(seen) * len(seen))
    return ans