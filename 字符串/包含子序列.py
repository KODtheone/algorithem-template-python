#比较 两个列表, 判断b 是 a的子序列 (不连续); 无用
def ck_sub_list(a,b): #a - ['a','d'] b - []
    if b == []:    return True
    p = 0; l = len(b)  # b的长度,即需要被判定的长度
    for z in a:
        if z == b[p]:
            p += 1
            if p == l:  return True
    return False

# 加上返回 匹配到的 a的下标
# 例题: https://leetcode.cn/contest/biweekly-contest-140/problems/find-the-lexicographically-smallest-valid-sequence/
def ck_sub_list(a,b):
    a = list(a)
    b = list(b)
    ans = []
    if b == []:    return True
    p = 0; l = len(b)
    for i, z in enumerate(a):
        if z == b[p]:
            ans += i,
            p += 1
            if p == l:  return True, ans
    return False, i