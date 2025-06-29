"""
例题:https://leetcode.cn/problems/minimum-time-to-revert-word-to-initial-state-ii/solutions/2630932/z-han-shu-kuo-zhan-kmp-by-endlesscheng-w44j/


"""
# 获得z box:
##2024年4月13日21:41:49, 这个具体用法没写清楚,需要补充...
# 2024年10月15日23:28:16  z函数:  s 的后缀与 s 的 LCP（最长公共前缀）长度，即 Z 函数（扩展 KMP）
# 即: zbox的说明  z[0] 本来应该是s的长度, 因为从0开始的后缀就是s本身, 但是定义上, z[0] 是 0; z[1]表示 s[1:] 与 s 的 LCP 长度
def zfun(s):
    n = len(s)
    z = [0] * n
    l = r = 0  # z box 的左右边界
    for i in range(1, n):
        if i <= r:  # i在 z box 内
            z[i] = min(z[i - l], r - i + 1)  ##z函数的核心思想
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            l, r = i, i + z[i]
            z[i] += 1
    return z

s = "abababzabababab"
zbox = zfun(s)
print(zbox)


#应用:  可以匹配前后缀
##遍历一次 可以得到 z 的所有值;  后面的具体k不重要,只是判断最早的一次,满足if i % k == 0 and z[i] == n - i: 罢了,即说明后面到结尾都匹配的前缀
class Solution:
    def minimumTimeToInitialState(self, s: str, k: int) -> int:
        n = len(s)
        z = [0] * n
        #abababzabababab
        #可视化 https://personal.utdallas.edu/~besp/demo/John2010/z-algorithm.htm
        l = r = 0 #z box 的左右边界
        for i in range(1, n):
            if i <= r:  #i在 z box 内
                z[i] = min(z[i - l], r - i + 1) ##z函数的核心思想
            #后面继续暴力匹配; 全靠核心初始化z[i],让匹配窗口单向向右滑动,O(n**2)变成了O(n)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                l, r = i, i + z[i]
                z[i] += 1
            print(z)
            if i % k == 0 and z[i] == n - i:
                return i // k
        return (n - 1) // k + 1

s = 'abababzabababab'
s = "aaaaaaaaz"
k = 1
print(Solution().minimumTimeToInitialState(s,k))
