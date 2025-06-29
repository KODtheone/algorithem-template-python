'''
2024年8月10日23:37:54 3234. 统计 1 显著的字符串的数量
https://leetcode.cn/problems/count-the-number-of-substrings-with-dominant-ones/solutions/2860198/mei-ju-zi-chuan-zhong-de-0-de-ge-shu-pyt-c654/

观察数据范围  比较不常见, 猜测是 O(n* sqrt(n))
把0出现的位置放进列表里面, 第二层循环放 这个, 不会超过 sqrt(n)
ans的增加比较类似贡献法 ,需要根据前个0的位置来推公式计算...
'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        a = [i for i, b in enumerate(s) if b == '0']
        tot1 = n - len(a)
        a.append(n)  # 哨兵
        ans = i = 0  # >= left 的第一个 0 的下标是 a[i]
        for left, b in enumerate(s):
            if b == '1':
                ans += a[i] - left  # 不含 0 的子串个数
            for k in range(i, len(a) - 1):
                cnt0 = k - i + 1
                if cnt0 * cnt0 > tot1:
                    break
                cnt1 = a[k] - left - (k - i)
                # 可以改成手动比大小，那样更快
                ans += max(a[k + 1] - a[k] - max(cnt0 * cnt0 - cnt1, 0), 0)
            if b == '0':
                i += 1  # 这个 0 后面不会再枚举到了
        return ans