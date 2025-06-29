'''
2024年10月7日22:53:14   字符串哈希的技术
例题:3292. 形成目标字符串需要的最少字符串数 II
https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/

# 不是最好的方法 , 还是用ac自动机为好...
用途: 可以用来高效的判断两个字符串是否相等   将一段字符串转化成一个数字
有概率撞同 ,但是通常可以过

'''
from random import randint

# 部分示例...   我感觉是为了 防止直接存储字符串mle , 所以把字符串算成一个数字
n = len(target)
mod = 1070777777
mod = 1_070_777_777
base = randint(8 * 10 ** 8, 9 * 10 ** 8)  #
pow_base = [1] + [0] * n
pre_hash = [0] * (n + 1)
for i, b in enumerate(target):
    pow_base[i + 1] = pow_base[i] * base % mod
    pre_hash[i + 1] = (pre_hash[i] * base + ord(b)) % mod

def sub_hush(l, r):
    return (pre_hash[r] - pre_hash[l] * pow_base[r - l]) % mod

max_len = max(map(len, words))
sets = [set() for i in range(max_len)]
for w in words:
    h = 0
    for j, b in enumerate(w):
        h = (h * base + ord(b)) % mod
        sets[j].add(h)


# class   2024年10月12日13:00:41  from: https://leetcode.cn/problems/minimum-time-to-revert-word-to-initial-state-ii/solutions/2630932/z-han-shu-kuo-zhan-kmp-by-endlesscheng-w44j/
MOD = 1_070_777_777
BASE = randint(8 * 10 ** 8, 9 * 10 ** 8)  # 随机 BASE，防止 hack

class HashStr:
    def __init__(self, s:str):
        n = len(s)
        self.pow_base = [1] + [0] * n  # pow_base[i] = BASE^i
        self.pre_hash = [0] * (n + 1)  # 前缀哈希值 pre_hash[i] = hash(s[:i])
        for i, b in enumerate(s):
            self.pow_base[i + 1] = self.pow_base[i] * BASE % MOD
            self.pre_hash[i + 1] = (self.pre_hash[i] * BASE + ord(b)) % MOD  # 秦九韶算法计算多项式哈希

    def get_sub(self, l, r):
        r += 1
        return (self.pre_hash[r] - self.pre_hash[l] * self.pow_base[r-l]) % MOD
