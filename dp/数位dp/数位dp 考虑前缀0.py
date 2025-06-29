'''
单纯的可以枚举出所有的数字可能, 配合@cache 可以加速
例题: https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/
902. 最大为 N 的数字组合

时间复杂度 O(logn)
'''


#使用例:  可以在f()中增加参数, 相当于挂载一个结果数,用于最后的比较
#最后比较写在     if i == len(s):  return  条件判断
#例题:  https://www.lanqiao.cn/problems/16984/learning/?contest_id=170
###注意开区间,闭区间.   我都已经作对了,但是最后的区间,把L点给排除了导致错误...
# 功能: 在[0, n]中,有多少个数字,恰好有k个封闭图形(8两个, 4一个, 1零个...)
# 参数: n:int  k: int
##注意,因为000001 = 1 在普通的数位dp里可以当做等价,但是在这里计算封闭取,就不能随便叫前导零了!
from functools import cache

n =1234435345234324324
k = 3

n = 9
s = str(n)

@cache
def f(i: int, is_limit: bool, is_num: bool, kk: int) -> int:
    if i == len(s):
        return is_num and kk == k # 如果填了数字，则为 1 种合法方案
    res = 0
    if not is_num:  # 前面不填数字，那么可以跳过当前数位，也不填数字
        # is_limit 改为 False，因为没有填数字，位数都比 n 要短，自然不会受到 n 的约束
        # is_num 仍然为 False，因为没有填任何数字
        res = f(i + 1, False, False, 0)
    up = s[i] if is_limit else '9'  # 根据是否受到约束，决定可以填的数字的上限
    # 注意：对于一般的题目而言，如果此时 is_num 为 False，则必须从 1 开始枚举，由于本题 digits 没有 0，所以无需处理这种情况
    # for d in digits:  # 枚举要填入的数字 d  2024年1月14日22:55:28, 原题这里是使用的数字有限 如 digits = ["1","4","9"]
    for d in [str(x) for x in range(10)]:  # 枚举要填入的数字 d
        if d > up: break  # d 超过上限，由于 digits 是有序的，后面的 d 都会超过上限，故退出循环
        # is_limit：如果当前受到 n 的约束，且填的数字等于上限，那么后面仍然会受到 n 的约束
        # is_num 为 True，因为填了数字
        # if not is_num and d == "0":  #注意,这里0也被排除了 不然可以用下面
        #     continue
        if not is_num and d == "0" and i != len(s)-1:
            continue
        newk = 0 if d in {'1', '2', '3', '5', '7'} else 2 if d == '8' else 1
        res += f(i + 1, is_limit and d == up, True, kk + newk)
    return res
# return f(0, True, False)
print(f(0,True,False, 0))


#通用版
#功能: 在[0,n]内,有多少个数字?   实际其中的具体数字是不含前导零的,这个条件在做具体题目判断时候才有效...
#参数: n:int
n = 8
s = str(n)
@cache
def f(i: int, is_limit: bool, is_num: bool) -> int:
    if i == len(s):
        return int(is_num)  # 如果填了数字，则为 1 种合法方案
    res = 0
    if not is_num:  # 前面不填数字，那么可以跳过当前数位，也不填数字
        # is_limit 改为 False，因为没有填数字，位数都比 n 要短，自然不会受到 n 的约束
        # is_num 仍然为 False，因为没有填任何数字
        res = f(i + 1, False, False)
    up = s[i] if is_limit else '9'  # 根据是否受到约束，决定可以填的数字的上限
    # 注意：对于一般的题目而言，如果此时 is_num 为 False，则必须从 1 开始枚举，由于本题 digits 没有 0，所以无需处理这种情况
    # for d in digits:  # 枚举要填入的数字 d  2024年1月14日22:55:28, 原题这里是使用的数字有限 如 digits = ["1","4","9"]
    for d in [str(x) for x in range(10)]:  # 枚举要填入的数字 d
        if d > up: break  # d 超过上限，由于 digits 是有序的，后面的 d 都会超过上限，故退出循环
        # is_limit：如果当前受到 n 的约束，且填的数字等于上限，那么后面仍然会受到 n 的约束
        # is_num 为 True，因为填了数字
        # if not is_num and d == "0":  #注意,这里0也被排除了 不然可以用下面
        #     continue
        if not is_num and d == "0" and i != len(s)-1:
            continue
        #根据题意的判断
        res += f(i + 1, is_limit and d == up, True)
    return res
# return f(0, True, False)
print(f(0,True,False))  #31 0~20有21个数字  00到09 有10个数字

#纯享版
#参数: n:int
#功能: 在[1,n]内,有多少个数字?   实际其中的具体数字是不含前导零的,这个条件在做具体题目判断时候才有效...
n = 9999999999999999999999999
s = str(n)
@cache
def f(i = 0, is_limit = True, is_num = False) -> int:
    if i == len(s):
        return int(is_num)
    res = 0
    if not is_num:
        res = f(i + 1, False, False)
    low = 0 if is_num else 1
    up = int(s[i]) if is_limit else 9
    for d in range(low, up + 1):
        #根据题意的判断
        res += f(i + 1, is_limit and d == up, True)
    return res

print(f(0,True,False))

