'''
2024年2月21日10:47:23, 预留一个板位, 这东西我一直一知半解的...

参考: 字典树  trie（发音类似 "try"）,, 没错,就是这么拼写的    见例题: 208. 实现 Trie (前缀树)
https://leetcode.cn/problems/implement-trie-prefix-tree/solutions/717239/shi-xian-trie-qian-zhui-shu-by-leetcode-ti500/
字典树应用于 XOR 计算, 也可以叫做  01 trie:  421. 数组中两个数的最大异或值
https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/

'''
from collections import defaultdict

#2024年4月3日10:41:09, 字典树当了好几个第四题了,必须掌握一波
##最简单的字典树模板:   根据words 里的内容,生成一个树;  查看word这个单词, 它是不是属于树中 ;;  稍微扩展一下:  树中的每个结点,保存一个东西
class TrieNode:
    __slots__ = 'son', 'x'   #x 就是保存的something
    def __init__(self):
        self.son = defaultdict(TrieNode)  #说明son是和自己一样的东西
        self.x = None
#上面的class写在外面  下面就直接接题目的class, 总之,下面给入了 words表 和 qword表
def question(words, qword):
    root = TrieNode()
    #建树
    for w in words:
        cur = root
        for c in w:
            # if c not in cur.son:  #(default结构使得这句不需要了,可#)
            #     cur.son[c] = TrieNode() #新路径
            cur = cur.son[c]    #移动指针
            #if ...
                # cur.x = ... #根据题目要求更新保存的东西
    #查询
    ans = []
    for q in qword:
        cur = root
        for c in q:
            if c not in cur.son:
                break
            cur = cur.son[c]  #一步一步树的最后
        ans += cur.x  #打个比方,需要查的是x里存的东西
    return ans


# 变体:  分开add word 和 query word;
class TrieNode:
    __slots__ = 'son', 'x'   #x 就是保存的something
    def __init__(self):
        self.son = defaultdict(TrieNode)  #说明son是和自己一样的东西
        self.x = None

# 注意作用域!  这部分还是要写进Solution 里面
root = TrieNode()  #还是要初始一个切入点,抓手
def add(word):
    cur = root
    for c in word:
        cur = cur.son[c]    #移动指针
        #if ...
            # cur.x = ... #根据题目要求更新保存的东西
#查询
# ans = []
def query(word):
    cur = root
    for c in word:
        if c not in cur.son:
            break
        cur = cur.son[c]  #一步一步树的最后
    return cur.x  #打个比方,需要差的是x里存的东西


#例题:https://leetcode.cn/problems/count-prefix-and-suffix-pairs-ii/solutions/2644160/z-han-shu-zi-dian-shu-pythonjavacgo-by-e-5c2v/
#3045. 统计前后缀下标对 II
#感觉不是很通用,所以这里直接放原题了
from collections import defaultdict
from typing import List

class Node:
    __slots__ = "son", "cnt"
    def __init__(self):
        # self.son = dict()
        self.son = defaultdict(Node)
        self.cnt = 0

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        root = Node()
        for s in words:
            cur = root
            for p in zip(s, reversed(s)):
                if p not in cur.son:
                    cur.son[p] = Node()
                cur = cur.son[p]
                ans += cur.cnt
            cur.cnt += 1
        # print(root, root.son, root.cnt)  #因为是树,所以看不到,非要看的话,自己写  def __str__(self):
        # print(root, root.son,root.son[('a', 'a')].son, root.cnt) ##('a','a') 不一定存在,所以还是defaultlist好..,
        return ans