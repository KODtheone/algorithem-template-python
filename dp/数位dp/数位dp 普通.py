from functools import cache
"""
最普通,当枚举用
"""
#纯享版
#参数: high 上限数字
#功能 从0 到 high 有多少个数字?
# 注解: 这个i是从最高位开始往后的,所以入口的 limit_high = True
high = 200
n = str(high)    #str()是为了方便枚举每一位 int(s[i])
@cache
def fun(i = 0, limit_high = True):  # i:位
    if i == len(n): return 1
    res = 0
    up = int(n[i]) if limit_high else 9
    for d in range(up + 1):
        #题意判断
        res += fun(i + 1, limit_high and d == up)
    return res
# return fun(0, True)

ans = fun(0, True)
fun.cache_clear()
print(ans)

'''
单纯的可以枚举出所有的数字可能, 配合@cache 可以加速
'''


@cache
def f(i: int, is_limit: bool, is_num: bool) -> int:
    if i == len(high): return int(is_num)  # 如果填了数字，则为 1 种合法方案
    res = 0
    up = n[i] if is_limit else '9'  # 根据是否受到约束，决定可以填的数字的上限
    # 注意：对于一般的题目而言，如果此时 is_num 为 False，则必须从 1 开始枚举，由于本题 digits 没有 0，所以无需处理这种情况
    # for d in digits:  # 枚举要填入的数字 d  2024年1月14日22:55:28, 原题这里是使用的数字有限 如 digits = ["1","4","9"]
    for d in [str(x) for x in range(10)]:  # 枚举要填入的数字 d
        if d > up: break  # d 超过上限，由于 digits 是有序的，后面的 d 都会超过上限，故退出循环
        # is_limit：如果当前受到 n 的约束，且填的数字等于上限，那么后面仍然会受到 n 的约束
        # is_num 为 True，因为填了数字
        res += f(i + 1, is_limit and d == up, True)
    return res
# return f(0, True, False)
# print(f(0,True,False))  #124  从0到123 有124个数字

# 纯享版
# #外部条件 数到最大数, high
high = 200
n = str(high)

@cache
def f(i = 0, is_limit = True, is_num = False) -> int:
    if i == len(high): return int(is_num)
    res = 0
    up = n[i] if is_limit else '9'
    for d in [str(x) for x in range(10)]:  
        if d > up: break
        res += f(i + 1, is_limit and d == up, True)
    return res

