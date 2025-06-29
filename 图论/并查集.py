#板子形式, 一个class,未封装, 调用类内函数
#2024年4月16日10:24:25,整理完成
'''
2024年4月7日14:18:46, 亡羊补牢的板子
题目: 今天上午的周赛第四题: https://leetcode.cn/problems/minimum-cost-walk-in-weighted-graph/submissions/520898535/
#重合方法: @cache + dfs
#并查集相对于 dfs的好处 : 可以一遍建立,一边查询   而dfs虽然O()小,但是只能先完全建立,之后再查

Disjoint Set Union   (dsu)
'''
#功能:  给出n个结点, 用edges 给出两两node无向相连;  查询任意两个点,相连通出1,不连通出-1
#输入及使用:  n个点.  对形成图的edges数据,分别执行union(); query查询两个点是不是属于同组
#三个输入数据: n, edges二维数列, querys 二维数列
#注意, 在union的时候,本质是 链子式的添加,所以其实都不需要比较x,y的大小, 随便赋值给谁都行!
class UnionFind:
    def __init__(self, n: int):  # 初始 n, n个点的图
        self.fa = [i for i in range(n)]
        self.x = [None] * n  #附带保存的结果结构 #扩一维
        # self.val = [-1] * n  #-1 & x = x

    def find(self, x: int) -> int:
        if self.fa[x] == x:
            return x
        # return self.find(self.fa[x]) #等价;总之就是递归找最小祖先
        self.fa[x] = self.find(self.fa[x])  ###神奇的地方!!! 修改之后,速度快了10倍,从3000ms到300ms ??? 题目: 2316 https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
        return self.fa[x]

    def union(self, x: int, y: int, w = 0): #edges中 x和y连接
        x = self.find(x)   #找到最小祖先
        y = self.find(y)
        self.fa[y] = x  #  **链子式的添加; 可能的py语言优化, 类似ans = max(ans,x)...大概也不需要,max问题是因为py的max()有问题
        ### self.x 执行一些相应的记录操作
        # self.val[x] = self.val[x] & self.val[y] & w

    def query(self, x, y) -> int:   #查x和y是否联通
        # if x == y : #特判
        #     return 0
        if (a:=self.find(x)) == self.find(y): #同一个祖先,说明在一个集合里
            return 1
            # return self.x[a]
        return -1
#时间复杂度：O((n+m+q)log n)，其中 m 为 edges的长度，query 的长度。 ??
#空间复杂度：O(n+m)。返回值不计入。

# 纯享版
class Uf:
    def __init__(self, n: int):
        self.fa = [i for i in range(n)]
        self.x = [None] * n

    def find(self, x: int) -> int:
        if self.fa[x] == x:
            return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x: int, y: int, w = 0):
        x = self.find(x)
        y = self.find(y)
        self.fa[y] = x
        # 对self.x的操作

    def query(self, x, y) -> int:
        if (a:=self.find(x)) == self.find(y):
            return 1
        return -1


# 补充功能:  在建立时,顺便统计联通块内点的个数; 实际就是添加一个self.x数据 , 不写代码了, 见: 笔记(0)121,并查集; 力扣2316. 统计无向图中无法互相到达点对数; 我自己的提交
# https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
#纯享版
# 2024年7月29日10:54:56, 调整完成  功能: 1, query 两个点是否联通  2, getsize 返回这个点的对应集的 相连个数
class Uf:
    def __init__(self, n: int):
        self.fa = [i for i in range(n)]
        self.ns = [1] * n

    def find(self, x: int) -> int:
        if self.fa[x] == x:
            return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.ns[x] += self.ns[y]
            self.fa[y] = x

    def query(self, a, b):
        return self.find(a) == self.find(b)

    def get_size(self, x) -> int:
        return self.ns[self.find(x)]


# 2025-5-18 14:04:17  增加 集合个数： self.cyc 的统计;   原理，每次成功union， self.cyc -= 1;   所以, 最后返回 self.cyc
'''
例题 https://leetcode.cn/problems/minimum-swaps-to-sort-by-digit-sum/
 
'''
class Uf:
    def __init__(self, n: int):
        self.fa = [i for i in range(n)]
        self.ns = [1] * n
        self.cyc = n

    def find(self, x: int) -> int:
        if self.fa[x] == x:
            return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.ns[x] += self.ns[y]
            self.fa[y] = x
            self.cyc -= 1

    def query(self, a, b):
        return self.find(a) == self.find(b)

    def get_size(self, x) -> int:
        return self.ns[self.find(x)]



