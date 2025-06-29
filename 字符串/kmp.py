# 输入: text-被找str  pattern-从text里找
# 输出:返回所有找到的idx列表; 例如[1,3,4] 从text的 第1,3,4位都是一个pattern的开头

def kmp(text: str, pattern: str) :
    m = len(pattern)
    pi = [0] * m
    c = 0
    for i in range(1, m):
        v = pattern[i]
        while c and pattern[c] != v:
            c = pi[c - 1]
        if pattern[c] == v:
            c += 1
        pi[i] = c

    res = []
    c = 0
    for i, v in enumerate(text):
        v = text[i]
        while c and pattern[c] != v:
            c = pi[c - 1]
        if pattern[c] == v:
            c += 1
        if c == len(pattern):
            res.append(i - m + 1)
            c = pi[c - 1]
    return res

a = "aaabaaa"
b = "b"
b = "aab"
print(kmp(a,b))