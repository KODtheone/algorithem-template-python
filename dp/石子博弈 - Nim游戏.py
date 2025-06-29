'''
2024年7月18日14:13:13,  一种比较统一套路的题目
可以划分为dp问题
例题:https://codeforces.com/gym/105239/problem/H
可以先化简为, 只有一堆石子, 谁赢, 然后,来的第二堆石子... 然后xor 只要有一次必赢,就是先手必赢
# 然后,三个纬度的, 分别来进行,我感觉我写的有问题,但是,可能题解的n**3解法,真的就是这个意思,反正是过了... https://codeforces.com/gym/105239/submission/271180102
高端解法 Grundy numbers  参考: https://www.geeksforgeeks.org/combinatorial-game-theory-set-3-grundy-numbers-numbers-and-mex/

分离经典问题: (Nim游戏)
 现在有一堆石头, 共有x个,  有a,b两个玩家, 每次可以从石头堆里取出 c = {c1, c2, c3,... cn} 一个列表作为可选项...  个石头,  轮流进行,谁无法
 继续谁就输了, 在a,b都使用最佳策略的情况下,最后的胜利者是谁?

 另外例子: https://leetcode.cn/problems/stone-game-iv/submissions/547775476/  我过了

'''
# 参数: n: int 石头个数   c: list[int] 可选择拿去数
def nim(n : int, c: list[int]):
    c.sort()
    dp = [False] * (n + 1)
    for i in range(1, n + 1):
        for j in c:
            ts = i - j
            if ts < 0: break
            if dp[ts] == False:
                dp[i] = True; break
    return dp[-1]

n = 10
c = [2, 3]
print(nim(n, c))