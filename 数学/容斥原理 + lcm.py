'''
例题:https://leetcode.cn/problems/kth-smallest-amount-with-single-denomination-combination/description/
3116. 单面值组合的第 K 小金额
给你一个整数数组 coins 表示不同面额的硬币，另给你一个整数 k 。
你有无限量的每种面额的硬币。但是，你 不能 组合使用不同面额的硬币。
返回使用这些硬币能制造的 第 kth 小 金额。

#用给出的n种coins 生成一个  n个元素容斥公式
##和乘法表中的第k大元素是完全不同的方法...

补充 基本公式: 容斥原理:   A ∪ B ∪ C = A + B + C - A ∩ B - A ∩ C - B ∩ C + A ∩ B ∩ C
2024年8月16日16:22:24  解释说明  容斥的递推公式   st存储相当于 x1& x2 & x3... 的项, 且, 序号为偶数时, 系数为负的.
只有一个coin元素x1  st为空, 就把  x1放进去  x1 系数为正的.  x2来了,  st 多了 -x1& x2, x2,   x3再来, 先跟老的st做运算

后面的计算部分, 例如 m = 100  对于st里面的一项, sti = 15;  m//sti = 100 // 15 = 6,包含了6个  系数为(-1) ** i = -1 * (-1) = 1
sum(((-1) ** i) * (m // x) for i, x in enumerate(st)) 计算的是m包含的项数之和, 当其==k时, 对应m为所求
'''
##本题中 合并两个集合的方式为 lcm(a,b) 而计算数量是,需要 m // lcm(x,y,z) 所以还需要一个fun2来计算结果
#功能   输入 数字列表nums 作为所有元素, 生成一个stack其中的值都是根据容斥算出来的lcm
#输入: nums
def fun(st, x):
    res = []
    for c in st:
        res += [lcm(c, x)]
    return res

stack = []
for x in nums:
    stack += fun(stack, x) + [x]  #刚好完美的完成了衍生,根据位置奇偶性决定正负号

def fun2(st, m):
    return sum(((-1) ** i) * (m // x) for i, x in enumerate(st))
    ###要把 m//x保护起来! 不然m是负数, 就算错了...  -8//3 = -3

############
#例题:https://leetcode.cn/problems/ugly-number-iii/description/
# 1201. 丑数 III的总体程序
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l = 0
        r = min(a,b,c) * n

        def fun(st, x):
            res = []
            for c in st:
                res += [lcm(c,x)]
            return res

        def fun2(st,m):
            return  sum(((-1)**i) *(m//x) for i,x in enumerate(st))
            ###要把 m//x保护起来! 不然m是负数, 就算错了...  -8//3 = -3

        stack = []
        for x in {a,b,c}:
            stack += fun(stack,x) + [x]

        def check(m):
            res = fun2(stack,m)
            return res >= n  # 或者 return False

        def bs(l, r):
            while l < r:
                mid = (l + r) >> 1
                if check(mid):
                    r = mid
                else:
                    l = mid + 1
            return r  ## r = l 为bisect_right  或者  return mid  为bisect_left
        return bs(l,r)

