'''
2024年7月23日16:07:15
题目来自: https://atcoder.jp/contests/abc363/tasks/abc363_c
# 需要注意 大量的切片和  [::-1] 操作,会导致超时...

'''

# 参数 s : 前提,先排序    s是需要进行全排列的列表 ,通过交换实现;  本体是字母, 数字应该也可以的
# 功能:  使用时候是原地修改s, 所以要配合一个while 1 来使用
s = sorted()
def next_permutation(s):
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i + 1]:
            break
    else:
        return False
    for j in range(len(s) - 1, i, -1):
        if s[i] < s[j]:
            break
    s[i], s[j] = s[j], s[i]
    s[i + 1:] = s[:i - len(s):-1]
    return True