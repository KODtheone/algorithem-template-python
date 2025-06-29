'''
2024年1月16日16:31:53 矩阵右旋转(顺时针)90度:   box = [*zip(*box[::-1])]
矩阵右旋转(顺时针)90度:   box = [*zip(*box[::-1])]
box[:] = [row[::-1] for row in zip(*box)]   等价
更正确: box[:] = [list(row[::-1]) for row in zip(*box)]      #多次执行,可以转 90度, 180度 270度
注意, zip出来的东西是 tuple 也就是 () 包围的.  要想形式符合 []  那就要对zip包的[x]  for x in zip
#*的作用就是单纯的解包  [1,2,3]  * 之后, 变成 1,2,3  没法单独付给一个值  也不可以 a,b,c = *[1,2,3]
因为这种形式的赋值, 正确的使用方式就是 a,b,c = [1,2,3]        ##貌似单独*m 来开苞没有用, 只能配合着zip来用
单独*x 可以print  但是不能单独写,不然 can't use starred expression here

btw, 双星号**，用于展开字典。
普通转置: box = list(zip(*box))
'''
grid = [[1, 2]]
grid = [*zip(*grid[::-1])]  #(顺时针)90度
print(grid)

# 转置
grid = list(zip(*grid))
'''
2024年6月25日20:04:46 增加矩阵切割
来自题目:3197. 包含所有 1 的最小矩形面积 II https://leetcode.cn/problems/find-the-minimum-area-to-cover-all-ones-ii/description/
2024年6月25日22:15:28,这个写的似乎复杂了,应该可以简化的
'''
# 功能:
# 参数: 例如 0,0,  3, 3 grid  提取 0,0 为左上角 3,3为 右下角的grid子矩阵
# def cut(il, jl, ir, jr, grid):
#     nm, nn = ir - il + 1, jr - jl + 1
#     ng = [[0] * nn for i in range(nm)]
#     for i in range(nm):
#         for j in range(nn):
#             ng[i][j] = grid[il+i][jl+j]
#     return ng

# 修改;  确实更好,时间略微提升了
def cut(il, ir, jl, jr, grid):
    nm= ir - il + 1
    ng = [0] * nm
    for i in range(nm):
        ng[i] = grid[il+i][jl:jr+1]
    return ng
