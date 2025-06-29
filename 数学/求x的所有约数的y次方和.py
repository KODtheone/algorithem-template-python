'''
2024年7月5日21:43:49  题目:
我算是完全独立做出来了...  踩玩了所有的坑...
分数取模方法很有用
# 本题主要利用等比序列求和
稍微需要注意下, y = 0的话需要特判...
## 出现了意料之外的wa之后 1, 找参数,看看有没有特别输入  2, 代码重打(消除typo)  3, 写naive 自己对版
'''
# 注意,本题的形式,不是直接给出x的值,而是把x分解好了给出
# 这样大概是为了方便应用 等比数列求和 的公式
times = 1  # 0有t, 1无t
if not times:
    times = ix()
for _ in range(times):
    n,k = ix()
    ans = 1
    if k == 0:
        for _ in range(n):
            v, c = ix()
            ans = (ans * (c+1))%mod
        print(ans)
        break
    for _ in range(n):
        v, c = ix()
        mp = (pow(v,k * (c+1), mod) - 1) * pow(pow(v, k, mod) - 1, mod - 2, mod)
        ans = ans * mp % mod
    print(ans)