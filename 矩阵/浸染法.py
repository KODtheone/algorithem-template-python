'''
2024年1月16日16:29:50,  求相邻的岛数量..   求特定相邻区域   并染色...
dfs bfs 都可以做   核心 状态转移  seen的剔除...
注意返回值的类型

例题:https://leetcode.cn/problems/coloring-a-border/solutions/1141382/bian-kuang-zhao-se-by-leetcode-solution-0h5l/?envType=list&envId=m7X6xrui
2024年7月14日21:02:10,  发现问题: 矩阵稍大, 比如 50 * 50 , 就会超时了.    按时说不应该的,状态数不过 2500, 就算是 500 也不过 250000,  但是却会-1073741571 (0xC00000FD)
代表 递归溢出...

用bfs比较好,虽然也不快,但是起码不会溢出了...
2024年7月15日15:46:35,  另外, 牛客这道题, 我在矩阵里面直接找值来做就过了, 但是我每次都deepcopy(grid) 然后染色来做,就导致超时了...   不知道是超时还是超空间,反正就是tm的超了...

'''
from typing import List

#使用目标  input  矩阵grid  初始点坐标 row,col    返回: 从row,col开始走,所有同值的格子都被感染.  返回 所有这些格子的列表
def infect(grid: List[List[int]], row: int, col: int) :
    m, n = len(grid), len(grid[0])
    o_val = grid[row][col]
    seen = set()
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ans = []

    def dfs(r, c):
        nonlocal ans
        if (r, c) in seen:
            return
        seen.add((r, c))
        if grid[r][c] != o_val:
            return
        ans += (r,c),
        for d0, d1 in d:
            if -1 < r + d0 < m and -1 < c + d1 < n:
                dfs(r + d0, c + d1)

    dfs(row, col)
    return ans

import sys
print(sys.getrecursionlimit()) # 1000
# sys.setrecursionlimit(10**10) #OverflowError: Python int too large to convert to C int
sys.setrecursionlimit(10**9)
# 但还是错误,


g = [[2,2,0],[2,3,2],[2,0,0],[2,2,0]]
g = [[0]*50 for i in range(50)]   # RecursionError: maximum recursion depth exceeded in comparison
a = 0
b = 1
print(infect(g, a, b)) #ok


'''
2024年7月23日21:00:38, 加一道类似的题目  淹没岛屿
https://atcoder.jp/contests/abc363/tasks/abc363_e
# 方法: 用一个最小堆   一开始把靠边的加入堆, 然后,最外层扫描时间, 如果能弹出, 就入新的能连接的
代码如下...
'''
from heapq import*
(h,w,y),*A = [[*map(int,t.split())] for t in open(0)]
Q = []
seen = [[0]*w for _ in range(h)]
for i in range(h):
  for j in range(w):
    if i == 0 or i == h-1 or j == 0 or j == w-1:
      seen[i][j] = 1
      heappush(Q,(A[i][j],(i,j)))
ans = h*w
for t in range(1,y+1):
  while Q and Q[0][0] <= t:
    _,(i,j) = heappop(Q)
    ans -= 1
    for dx,dy in ((-1,0),(0,-1),(1,0),(0,1)):
      nx,ny = i+dx,j+dy
      if not (0 <= nx < h and 0 <= ny < w):
        continue
      if seen[nx][ny]:
        continue
      seen[nx][ny] = 1
      heappush(Q,(A[nx][ny],(nx,ny)))
  print(ans)