'''
例题:233. 数字 1 的个数  https://leetcode.cn/problems/number-of-digit-one/description/
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
'''

#问题:   给定一个整数 n，计算所有小于等于 n 的非负整数中数字 x 出现的个数。   注意, x!=0
#使用十进制, 因此x一定是0~9中的数字
#重述: 在 0 ~ num的所有数字中, 出现x( x!=0, 不然 0056属于非法数字, 需要另加考虑, 刨去前缀0...)的次数
#参数:

def fun(n: int, x) -> int:
    s = str(n)
    @cache
    def dfs(i = 0, ans = 0, is_limit = True) -> int:
        if i == len(s):   return ans
        res = 0
        up = int(s[i]) if is_limit else 9
        for d in range(up + 1):
            res += dfs(i + 1, ans + (d == x), is_limit and d == up)
        return res

    return dfs()