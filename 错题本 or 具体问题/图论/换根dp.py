'''
2024年8月4日16:42:09, 力扣又出了,不得不学了...   https://leetcode.cn/problems/time-taken-to-mark-all-nodes/ 3241. 标记所有节点需要的时间
让我今天来研究研究为什么没法通过吧,哦,大概有个想法,因为在最大值判断中有一个二重循环,所以虽然我@cache了,但还是O(n^n)的.    所以只能换根
# 第二类换根dp  难度2   atcoder上有更难的 第三类换根dp

老笔记:
71,换根dp   例题: https://leetcode.cn/problems/sum-of-distances-in-tree/solutions/2345592/tu-jie-yi-zhang-tu-miao-dong-huan-gen-dp-6bgb/   834. 树中距离之和
# 这个题是最基本的    有灵茶的详细题解
2024年3月30日20:46:26, 增加例题 : 2581. 统计可能的树根数目 https://leetcode.cn/problems/count-number-of-possible-root-nodes/
不过,这个换根dp的模板不太好些啊...       草莓奶昔倒是写了一套模板,但是很复杂...  https://github.com/981377660LMT/algorithm-study/blob/master/6_tree/%E7%BB%8F%E5%85%B8%E9%A2%98/%E5%90%8E%E5%BA%8Fdfs%E7%BB%9F%E8%AE%A1%E4%BF%A1%E6%81%AF/%E6%8D%A2%E6%A0%B9dp/Rerooting.py

'''
from typing import List

# 重点 ,  换根的转移方程;  怪不得叫换根dp, 因为核心还是dp转移方程

# 834. 树中距离之和
# 第一步: 计算树的深度, 用来算初始距离和; 顺便还好计算字数的规模 size   第二步: 进行换根操作  也是递归
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for i in range(n)]
        for a, b in edges:
            g[a] += b,
            g[b] += a,
        depths = [0] * n
        size = [1] * n

        def dfs(a=0, fa=-1, d=0):
            depths[a] = d
            for b in g[a]:
                if b == fa: continue
                dfs(b, a, d + 1)
                size[a] += size[b]  # 计算 和 递归 的顺序很重要  尤其是这种, 递归中, 计算值要保存给外部的情况

        dfs()
        ans = [0] * n
        ans[0] = sum(depths)

        # print(ans, size)
        def reroot(a=0, fa=-1):
            for b in g[a]:
                if b == fa: continue
                ans[b] = ans[a] + n - size[b] * 2
                reroot(b, a)  # 先计算,再递归,顺序不能乱!

        reroot()
        return ans


# 3241. 标记所有节点需要的时间
# 第一步, 依然是计算深度, 其实是路程, 因为有权重值了  第二步, 换根
'''
需要记录三个信息: 子树最大深度, 次大深度, 通过哪个结点到达最大深度
有点像 拼接两个图,计算最大直径的那个题.
最后最大深度的来源:   from_up  往上走到某节点再往下拐弯的路径长度 ( 这部分计算, 有点类似 m = max(m, t), 一直保留最大值就行了,不过,又是嵌入在dfs里面的 )
'''
class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        g = [[] for i in range(len(edges) + 1)]
        for a, b in edges:
            g[a] += b,
            g[b] += a,
        nodes = [None] * len(g) # dfs跑完, 外部存储的 node 信息

        def dfs(x=0, fa=-1):
            max_d = max_d2 = my = 0
            for y in g[x]:
                if y == fa: continue
                depth = dfs(y, x) + 2 - y % 2
                if depth > max_d:
                    max_d2 = max_d
                    max_d = depth
                    my = y
                elif depth > max_d2:
                    max_d2 = depth
            nodes[x] = (max_d, max_d2, my)  # 记录了那三种
            return max_d

        dfs()
        ans = [0] * len(g)

        def reroot(x=0, fa=-1, from_up=0):  # from_up 从上面累加的路程(权重)
            max_d, max_d2, my = nodes[x]
            ans[x] = max(from_up, max_d)
            w = 2 - x % 2
            for y in g[x]:
                if y == fa: continue
                reroot(y, x, max(from_up, max_d2 if y == my else max_d) + w)

        reroot()
        return ans