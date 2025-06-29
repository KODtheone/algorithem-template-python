"""
链接：https://ac.nowcoder.com/acm/contest/75766/E
输入n−1行，每行输入两个正整数,u,v，代表节点u和节点v有一条边连接。
"""
#随意叶子结点都可以当做root
#例如:   #实际上等价于 edges形式
'''
n = 4
1 2
1 3
1 4
'''
# 创建一个空字典来存储图
graph = {}
# 读取n-1行输入
# n = int(input("请输入节点数量："))
n = ix()
for _ in range(n - 1):
    # u, v = map(int, input("请输入两个连接的节点（u v）：").split())
    u, v = il()
    # 如果u不在图中，为其创建一个空列表
    if u not in graph:
        graph[u] = []
        # 如果v不在图中，为其创建一个空列表
    if v not in graph:
        graph[v] = []
        # 在u和v的列表中分别添加对方
    graph[u].append(v)
    graph[v].append(u)
print(graph)
# 输出图结构
# for node, neighbors in graph.items():
#     print(f"节点 {node} 与以下节点相连: {neighbors}")


'''
2024年7月31日15:45:02 一种cf上的建树, 题目:  https://codeforces.com/contest/1997/problem/D
a 结点值列表  a[i] = j   结点i的值为j  注意, 这是符合cf的从1开始编号(所以前面加了个空的[0])
g 连接图列表  g[i] = [a,b,c,,,,]  abc等是i的子节点
# 此题用dfs做会runtime error, 因此py貌似只能使用递推...  c++就可以递归,  cf还是太针对python了啊...
# 解法:  二分,  设能增加到mid 计算需要的增量,然后跑bfs验证子树都满足;  
'''
n = ix()
a = [0] + il()
g = [[] for _ in range(n + 1)]
for i, c in enumerate(il(), 2): g[c] += i,
# 归零:
n = ix()
a = il()
g = [[] for _ in range(n)]
for i, c in enumerate(il(), 1): g[c - 1] += i,
# 例题 核心程序如下: (读入的是归零序号)
times = 0  # 0有t, 1无t
if not times:
    times = ix()
for _ in range(times):
    n = ix()
    l = il()
    p = il()
    left, right = l[0], 2 * 10 ** 9 + 1
    d = [[] for _ in range(n)]
    for y, x in enumerate(p):   d[x - 1].append(y + 1)
    while left < right - 1:
        mid = (left + right) // 2
        st = [0]
        need = [0] * n
        need[0] = mid - l[0]
        while st:
            x = st.pop()
            if need[x] > 10 ** 9 or need[x] > l[x] and not d[x]:
                right = mid
                break
            for y in d[x]:
                st.append(y)
                if need[x] <= l[y]:
                    need[y] = need[x]
                else:
                    need[y] = need[x] + need[x] - l[y]
        else:
            left = mid
    print(left)






