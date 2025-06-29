'''
2024年8月19日22:45:46 https://leetcode.cn/problems/find-the-largest-palindrome-divisible-by-k/solutions/2884548/tong-yong-zuo-fa-jian-tu-dfsshu-chu-ju-t-m3pu/
3260. 找出最大的 N 位 K 回文数
注意  本题有本地运行bug
比如case 99999, 7 会遇到 'RecursionError: maximum recursion depth exceeded in comparison'; 而如果修改了 sys.setrecursionlimit(3005), 又会变成 '进程已结束，退出代码为 -1073741571 (0xC00000FD)'...
2024年8月31日11:07:46, bug已解决, 原因是py的版本太久,  更新到py3.12 就好了...

方法:   预处理 1000...  % k 的值, 方便查
在 第i为和 -1-i位 ,插入数字d时,  mod的余量变动为 j2= (j + d * (pow10[i] + pow10[-1 -i])) % k
判断一下, vis[i + 1][j2] 是否为false, 为true的话看过了; 并且dfs(i + 1, j2)能返回true, 说明这个数字是回文数
vis[i][j] 相当于一个查重, 如果走到i位, mod的余量j, 已经跑过了, 就不用继续,因为第一次跑时d值一定更大
可以用@cache来替代这个查重,但是灵茶说, cache更慢
时间复杂度：O(nkD)，其中 D=10。
'''

class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        pow10 = [1] * n
        for i in range(1, n):
            pow10[i] = pow10[i - 1] * 10 % k
        ans = [0] * n
        m = (n + 1) // 2
        vis = [[False] * k for i in range(m + 1)]
        def dfs(i, j):
            if i == m: return j == 0
            vis[i][j] = True
            for d in range(10)[::-1]:
                if n % 2 and i == m - 1:
                    j2 = (j + d * pow10[i]) % k
                else:j2= (j + d * (pow10[i] + pow10[-1 -i])) % k
                if not vis[i + 1][j2] and dfs(i +1, j2):
                    ans[i] = ans[-1-i] = str(d)
                    return True
            return False
        dfs(0,0)
        return ''.join(ans)