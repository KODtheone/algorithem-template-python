'''
2024年6月24日22:28:59
在例题: 3193. 统计逆序对的数目  https://leetcode.cn/problems/count-the-number-of-inversions/description/
中,注意到了一种有趣的递推三角形生成:
1
1 1
1 2 2 1
1 3 5 6 5 3 1
...
不像杨辉三角形那样能直接算出第n行
而是将 n-1行滚动相加n次,获得第n行

生成函数如下
应用, 查询res[99][7] 表示 99+2个数字 组成的全排列数列, 其中带有 7个逆序对的排列情况数
##  对求解原题似乎没什么帮助...  因为原题不只一个要求 .  如果只有一个要求, 例如 [101, 7] 那可以用这个res表直接得到解...
'''
mod = 10**9+7  # 因为数字太大,所以加了mod

# 工作方式: 打表
def fun(a, b):  # 将数组a 滚动相加n次
    na = a + [0] * b  # 滑窗底座
    ans = [0] * len(na)
    t = 0
    for i, x in enumerate(na):
        l = max(-1, i - b - 1)
        t = (t + x - na[l])%mod
        ans[i] = t
    return ans

g = [1]
res = [g]
t = 1
for i in range(10):   #选择循环次数
    g = fun(g, t)
    t += 1
    res += g,
print(res)
# print(res[99][7])
# 使用 例如查询  n个数组成的数列,  k个逆序对, 则: print(res[n-2][x])

'''
2024年6月26日11:07:33  打表的实用性不高  如果n = 1000 直接爆内存...   例如: 629. K 个逆序对数组
所以,还不如 dfs用什么生成什么...
或者,我尝试一下不将每组结果记录在dfs里,而是单纯的滚动结果
'''
# 纯享版
# 功能 参数:   返回n个数组成的数列,有k个逆序对 的情况数
mod = 10 ** 9 + 7  #注意mod是什么
def cn(n, k):
    f = [1] + [0] * k
    for i in range(1, n + 1):
        g = [0] * (k + 1)
        for j in range(k + 1):
            g[j] = (g[j - 1] if j - 1 >= 0 else 0) - (f[j - i] if j - i >= 0 else 0) + f[j]
            g[j] %= mod
        f = g
    return f[k]

print(cn(100,100))



## 废弃: 用打表方法做,但是会超时  n = k = 1000 时
# def cn(n, k):
#     mod = 10 ** 9 + 7
#     def fun(a, b):
#         na = a + [0] * b
#         ans = [0] * len(na)
#         t = 0
#         for i, x in enumerate(na):
#             l = max(-1, i - b - 1)
#             t = (t + x - na[l]) % mod
#             ans[i] = t
#         return ans
#
#     g = [1]
#     t = 1
#     for i in range(n-1):
#         g = fun(g, t)
#         t += 1
#     return g[k]
#
# print(cn(3,2))