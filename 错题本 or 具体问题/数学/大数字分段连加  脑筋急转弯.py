''''
题目: https://atcoder.jp/contests/abc379/tasks/abc379_e
问题陈述
给定一个长度为N的字符串S，该字符串由从1到9的数字组成。
对于每一对整数(i, j)（其中1 ≤ i ≤ j ≤ N），定义函数f(i, j)为将字符串S中从第i个字符到第j个字符（包含i和j）的子串解释为十进制整数后得到的值。
要求计算以下求和：
∑ (从 i=1 到 N)∑ (从 j=i 到 N) f(i, j)
即，对所有可能的子串（从字符串的开头到结尾）进行求和。

限制因素
1 ≤ N ≤ 2 × 10^5
N是一个整数。
S是长度为N的字符串，由从1到9的数字组成。
输入样本 1
3
379

输出样本 1
514

解释：
答案是通过以下方式计算得出的：
f(1,1) + f(1,2) + f(1,3) + f(2,2) + f(2,3) + f(3,3)
= 3 + 37 + 379 + 7 + 79 + 9
= 514

2024年11月9日22:05:27,  题意看样本就行了, 我发现了加的规律 ,但是没想到进一步, 处理超大数字的方法

PS: 一个应该放下问题的点 c++里, ll 也不到 10 ** 20 位数字, 而这个输出数字位数明显超过了, 所以不可能全部使用数字计算...
最大s 位 9 * (1 + 2 * 10 ** 5) * (2 * 10 ** 5) // 2  大约位 18 * 10 ** 10

'''

N = int(input())
S = input()
dp = [0] * N
s = 0
for n in range(N):
    s += int(S[n]) * (n + 1)
    dp[n] = s
# print(dp)
ans = []
for n in range(N)[::-1]:
    if n >= 1:
        ans.append(dp[n] % 10)
        dp[n - 1] += dp[n] // 10
    else:
        ans.append(dp[n])
print(''.join(map(str, ans[::-1])))


'''测试'''
N = 2 * 10 ** 5
S = '9' * 2 * 10 ** 5
dp = [0] * N
s = 0
for n in range(N):
    s += int(S[n]) * (n + 1)
    dp[n] = s
# print(dp)
ans = []
for n in range(N)[::-1]:
    if n >= 1:
        ans.append(dp[n] % 10)
        dp[n - 1] += dp[n] // 10
    else:
        ans.append(dp[n])
print(''.join(map(str, ans[::-1])))
