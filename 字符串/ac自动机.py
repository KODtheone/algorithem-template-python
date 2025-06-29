'''
2024年7月7日13:17:31  AhoCorasick
题目:  https://leetcode.cn/problems/construct-string-with-minimum-cost/description/
从  cherry_77 的答案上抄写的模板

2024年7月11日15:51:09,  注意,此模板被hack...

原理: https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/solutions/2917929/ac-zi-dong-ji-pythonjavacgo-by-endlessch-hcqk/
对比以下两个 target 的前缀：
aabcd，需要连接 2 个 words[i] 的前缀 aa 和 bcd。
aab，需要连接多少个前缀？可以肯定的是，答案一定不会比 2 还大，因为我们把 aabcd 末尾的 cd 去掉就可以得到 aab。这仍然是 2 个前缀的连接。
根据上述讨论，如果用 f[i] 表示 target 的长为 i 的前缀需要连接的最少字符串数量，那么 f[i]≤f[i+1] 一定成立。
既然 f 是有序数组，那么对于 f[i]，我们只需要知道最小的 j，满足从 target[j] 到 target[i−1] 是某个 words[i] 的前缀。
也就是说，匹配的 words[i] 的前缀要尽量长。这正是 AC 自动机的应用。


'''
# 构造:  给入 words  和 costs  ;ac = AhoCorasick(words, costs)
# 查询: ac.search(target)
# 小碎片, words[i] 的花费是 costs[i],   求用所有words中的碎片拼凑出target的最小代价
class TrieNode:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.cost = float('inf')
        self.length = 0  # 单词长度
class Ac:
    def __init__(self, words, costs):
        self.root = TrieNode()
        self.build_trie(words, costs)
        self.build_failure_pointers()

    def build_trie(self, words, costs):
        for word, cost in zip(words, costs):
            current = self.root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            current.cost = min(current.cost, cost)  # 记录最小成本
            current.length = len(word)  # 记录单词长度

    def build_failure_pointers(self):
        from collections import deque
        queue = deque([self.root])
        while queue:
            current = queue.popleft()

            for char, child in current.children.items():
                queue.append(child)
                fail = current.fail
                while fail and char not in fail.children:
                    fail = fail.fail
                child.fail = fail.children[char] if fail else self.root

    def search(self, target):
        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        current = self.root
        for i in range(n):
            while current and target[i] not in current.children:
                current = current.fail
            if current:
                current = current.children[target[i]]
                temp = current
                while temp != self.root:
                    if temp.cost < float('inf'):
                        start = i - temp.length + 1
                        dp[i + 1] = min(dp[i + 1], dp[start] + temp.cost)
                    temp = temp.fail
            else:
                current = self.root
        return dp[n] if dp[n] != float('inf') else -1

# test
word = ["a"]
cost = [2]
target = "aaa"
a = Ac(word, cost)
print(a.search(target))

'''
板子2  ,  灵茶的 
例题:3292. 形成目标字符串需要的最少字符串数 II  

https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/

'''

# 未整理



