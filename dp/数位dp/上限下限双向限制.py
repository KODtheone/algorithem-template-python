#2024年4月16日10:24:38,整理中
'''
例题:https://leetcode.cn/problems/count-the-number-of-powerful-integers/solutions/2595149/shu-wei-dp-shang-xia-jie-mo-ban-fu-ti-da-h6ci/
2999. 统计强大整数的数目
'''
from functools import cache

#专题模板; 功能 求出在 start 到 finish的数组之间,且每位数字最多为limit , 共有多少个结尾为s 的数字
#外参数: low: 下界数字的str形,补充了前导零; high: 上界数字的str形式;  s 结尾要匹配的数字, str形; limit 每位最大为limit:0~9;
#中间参数 n = len(high), 总位数;  diff = n - len(s)能自由填值的位数
#内参数: i: 当前dp的数位(注意,是倒着的,i= 0表示最高位); limit_low: bool 布尔型,判断位是否有下限;  limit_high 类似..
start = 10000
finish = 2000000
limit = 5
s = '1234'
#
low = str(start)
high = str(finish)
n = len(high)
low = '0' * (n - len(low)) + low  # 补前导零，和 high 对齐
diff = n - len(s)
@cache
def dfs(i: int, limit_low: bool, limit_high: bool) -> int:
    if i == n:  #i成功走完到最后一位了,说明构造数字成功
        return 1

    # 第 i 个数位可以从 lo 枚举到 hi
    # 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
    lo = int(low[i]) if limit_low else 0
    hi = int(high[i]) if limit_high else 9

    res = 0
    if i < diff:  # 枚举这个数位填什么
        for d in range(lo, min(hi, limit) + 1):
            res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
    else:  # 这个数位只能填 s[i-diff]
        x = int(s[i - diff])
        if lo <= x <= min(hi, limit):
            res = dfs(i + 1, limit_low and x == lo, limit_high and x == hi)
    return res

print(dfs(0, True, True))
# return dfs(0, True, True)

#整理版:
#纯享版
# 参数: low, high
# 功能: 在low到 high之间,有多少个数字
n = len(high)
low = '0' * (n - len(low)) + low
@cache
def dfs(i = 0, limit_low = True, limit_high = True) -> int:
    if i == n:
        return 1
    lo = int(low[i]) if limit_low else 0
    hi = int(high[i]) if limit_high else 9
    res = 0
    for d in range(lo, hi + 1):
        if 1:  #可能需要根据题意做判断
            res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
    return res

dfs.cache_clear()
#时间复杂度 O(n) n为最大数字位数n = len(high)


