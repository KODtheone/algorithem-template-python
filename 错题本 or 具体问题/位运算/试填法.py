'''
2024年9月20日11:27:49, 来自笔记
试填法系列问题:
 按难度正序排列:
  421. 数组中两个数的最大异或值    https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/description/
  3007. 价值和小于等于 K 的最大数字   https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/description/
  3145. 大数组元素的乘积     https://leetcode.cn/problems/find-products-of-elements-of-big-array/description/
##  数字非常大,  时间复杂度的判断不明显( 后两题)
#核心思路: k太大(10**15)  因此用二进制考虑  10**15 = 2**50  log2(k) 之后, 只需要考虑50位 还可以乘以一个O(n)  毕竟50不算是很大的常数

例题:   给你两个列表 ,  想从两个列表中各取一个数,  使得  这两个数的异或值最大
'''
from typing import List


# 例题:   给你两个列表 ,  想从两个列表中各取一个数,  使得  这两个数的异或值最大
# w 是最高位数
# mx = reduce(or_, a + b)
# w = mx.bit_length()

def findMaximumXOR(self, a: List[int], b: List[int], w: int) -> int:
    ans = mask = 0
    for i in range(w - 1, -1, -1):  # 从最高位开始枚举
        mask |= 1 << i
        new_ans = ans | (1 << i)  # 这个比特位可以是 1 吗？
        set_a = set(x & mask for x in a)  # 低于 i 的比特位置为 0
        for x in b:
            x &= mask  # 低于 i 的比特位置为 0
            if new_ans ^ x in set_a:
                ans = new_ans  # 这个比特位可以是 1
                break
    return ans

# 纯享版
def fm(self, a, b, w: int) -> int:
    ans = mask = 0
    for i in range(w)[::-1]:
        mask |= 1 << i
        new_ans = ans | (1 << i)
        set_a = set(x & mask for x in a)
        for x in b:
            x &= mask
            if new_ans ^ x in set_a:
                ans = new_ans
                break
    return ans
