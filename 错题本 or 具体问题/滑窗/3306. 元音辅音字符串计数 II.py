'''
3306. 元音辅音字符串计数 II
https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/
2024年9月29日13:02:40,  脑筋急转弯
正难则反  写一个  计算  >= k个辅音的滑窗 然后    >= k 个辅音 -   >= k + 1个辅音

## 注意 Counter直接比较有坑 ,速度慢 ,会被卡常...
while all(c[x] >= cc[x] for x in cc):    甚至也不行...
甚至不如
for x in cc:
    if c[x] < cc[x]:
        break

要写 while c['a'] > 0 and c['e'] > 0 and c['i'] > 0 and c['o'] > 0 and c['u'] > 0 and c['_'] >= k: 才能过...
也算是卡常过的, 或者说 没有被    卡常...       因为这里如果提前出问题, 会提前结束

# 脑筋急转弯  正难则反     奇妙恶心的卡常问题...


'''


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def f(w, k):
            n = len(w)
            l = ans = 0
            c = defaultdict(int)
            s = 6 - (k == 0)
            for r, x in enumerate(w):
                if x in "aieou":
                    c[x] += 1
                    if c[x] == 1: s -= 1
                else:
                    c['1'] += 1
                    if c['1'] == k:     s -= 1
                while s == 0:
                    t = w[l]
                    if t in "aieou":
                        c[t] -= 1
                        if c[t] == 0:  s += 1
                    else:
                        c['1'] -= 1
                        if c['1'] == k - 1: s += 1
                    l += 1
                ans += l
            return ans

        return f(word, k) - f(word, k + 1)
