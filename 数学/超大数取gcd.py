'''
https://ac.nowcoder.com/acm/contest/86034/D
一个数超级大  只能用字符串来展示那种  10**6 位的长度

# a,b 的gcd  =  a%b, b 的gcd;  而a%b 按位计算
2024年8月18日11:33:26, 包括, 大数取模mod
'''
import sys


# num是超大数,字符串型  改成int(num)print 都会卡一会那种
def mod(num, a):
    res = 0
    for i in range(0, len(num)):
        res = (res * 10 + int(num[i])) % a
    return res

ans = gcd(mod(a,b),b)

sys.set_int_max_str_digits(0)
# a = 10**(10**6)
# print(a)
# a = "1" + "0"*(10**6+ 1)
# print(a)    # 打字符串就很快了