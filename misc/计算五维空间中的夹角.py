import numpy as np

il = lambda: list(map(int, input().split()))
'''
输入样例:
0 0 1 2 0
17 0 9 2 0
0 0 5 9 0
'''
# 假设 a, b, c 是五维空间中的点，用坐标表示
a = np.array(il())
b = np.array(il())
c = np.array(il())

# 计算向量 ab 和 ac
ab = b - a
ac = c - a

# 计算向量间的夹角（以弧度为单位）
cos_angle = np.dot(ab, ac) / (np.linalg.norm(ab) * np.linalg.norm(ac))
angle_radians = np.arccos(cos_angle)
angle_degrees = np.degrees(angle_radians)

print(f"向量 ab 和 ac 之间的夹角是: {angle_degrees} 度")


'''
例题: https://codeforces.com/problemset/problem/850/A
但是很遗憾, codeforces 用不了 numpy
小羊的题解 https://codeforces.com/problemset/problem/850/A

'''
