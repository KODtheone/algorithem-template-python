'''
马拉车manacher算法
目前解决最大回文子串有以下几种常见解法：
1.暴力法O(n3)
2.中心扩散法O(n2)
3.hash+二分法O(n2)
4.动态规划O(n2)
5.manacher算法O(n)

原理视频:  https://www.bilibili.com/video/BV1Sx4y1k7jG

用途: O(n)判断最长回文子字符串
'''
# 参数 s: 待处理的字符串
# p列表: 添加# 之后 , 最长的回文子串的半径


def manacher(s):
    s = '#' + '#'.join(s) + '#'
    lens = len(s)
    p = [0] * lens
    mx = 0
    id = 0
    for i in range(lens):
        if mx > i:
            p[i] = min(mx - i, p[int(2 * id - i)])
        else:
            p[i] = 1
        while i - p[i] >= 0 and i + p[i] < lens and s[i - p[i]] == s[i + p[i]]:
            p[i] += 1
        if (i + p[i]) > mx:
            mx, id = i + p[i], i
    i_res = p.index(max(p))
    s_res = s[i_res - (p[i_res] - 1):i_res + p[i_res]]
    print(p)
    return max(p) - 1

print(manacher(''))
print(manacher(' '))
print(manacher('abab'))
print(manacher('abba'))
print(manacher('aaaaaaa'))
print(manacher('Is PAT&TAP symmetric?'))

'''
2025年3月2日09:04:10  扩展问题
给定一个字符串，求分割成回文子串  最少分割次数
例题 : 最少分割次数

'''