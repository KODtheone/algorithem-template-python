'''
2025年5月4日09:34:21， 例题忘记了，所以自己来写一个题意：
给一个arr， arri > 0, 代表可以跳arri步。问从0开始，一直跳出arr ， 即达到index = n， 最少需要多少步。
arri表示在第i个位置，最多可以跳到第i+arri个位置。

类似例题： https://atcoder.jp/contests/abc404/tasks/abc404_e

2025年5月4日10:06:17，找到了， 是这个跳跃游戏ii  https://leetcode.cn/problems/jump-game-ii/description/
'''
a = [9, 4, 1, 1, 4]

def solution(arr):
    arr = [1] + arr
    next_go = 0
    go = 1
    ans = -1
    for x in arr:
        go -= 1
        next_go = max(next_go - 1, x)
        if go == 0:
            ans += 1
            go = next_go
    return ans

print(solution(a))
