'''
2024年6月24日23:19:38, n个非负整数相加等于v, 有多少种情况
表面上挺复杂,但其实很简单
就是  3179. K 秒后第 N 个元素的值   https://leetcode.cn/problems/find-the-n-th-value-after-k-seconds/description/
累加的累加公式看起来复杂, 但其实子项永远都是等差数列,因此可以继续整合成等差数列形式     而根据题目中找出的规律 ,最后都可以用comb来计算得到...

2024年6月25日08:53:26, 这不就是插板法... 数字和v用v个小球, 分成n个数,当做n-1个板子,两个板子之间的小球数就是这个数字填多少

2024年10月5日21:00:21
插板法另一种应用 : 从 S={1,2,...,n}中选取 k 个数，使其没有两个数相邻， 求不同的选法数。?
例题: https://www.lanqiao.cn/problems/19862/learning/?contest_id=209
公式:  n 个 数字里面 , 取k个数, 且没有两个数相邻, 有多少种情况
    C(n - k + 1, k)

'''
from math import comb

#相对于原题 n = n - 1 v = k + 1
#参数:  n个非负整数相加等于v;  返回情况数
def vs(n: int, v: int) -> int:
    mod = 10**9+7
    ans = comb(v - 1 + n, n - 1)
    return ans % mod


print(vs(4, 32))