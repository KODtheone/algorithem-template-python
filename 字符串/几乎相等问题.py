'''
3302. 字典序最小的合法序列
https://leetcode.cn/problems/find-the-lexicographically-smallest-valid-sequence/description/
3303. 第一个几乎相等子字符串的下标
https://leetcode.cn/problems/find-the-occurrence-of-first-almost-equal-substring/description/

2024年10月12日12:28:05
 这两题的问题类似 , 都需要求 几乎相等的字符串, 定义:
如果一个字符串 x 修改 至多 一个字符会变成 y ，那么我们称它与 y 几乎相等 。

解法:  1, 前后缀分解 + 子序列匹配 + 贪心
2, 前后缀分解 + Z 数组
核心方法, 全后缀分解...

# 为什么不能用kmp: kmp是不能修改的   https://www.bilibili.com/video/BV1bjxyewEQV/
而且 kmp是子字符串 不是子序列
## 2024年10月12日12:48:03  注意 这两题的做法其实完全不一样   只有前后缀是一样的
第二题:  z函数秒了
 z函数的方向是刚好的,  而如果用kmp的话, kmp方向是一左一右的
'''